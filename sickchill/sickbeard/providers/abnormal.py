import re
from urllib.parse import urljoin

from requests.utils import dict_from_cookiejar

from sickchill.helper.common import convert_size, try_int
from sickchill.providers.torrent.TorrentProvider import TorrentProvider
from sickchill.sickbeard import logger, tvcache
from sickchill.sickbeard.bs4_parser import BS4Parser


class Provider(TorrentProvider):

    def __init__(self):

        # Provider Init
        super().__init__("ABNormal")

        # Credentials
        self.username = None
        self.password = None

        # Torrent Stats
        self.minseed = 0
        self.minleech = 0

        # URLs
        self.url = 'https://abnormal.ws'
        self.urls = {
            'login': urljoin(self.url, 'login.php'),
            'search': urljoin(self.url, 'torrents.php'),
        }

        # Proper Strings
        self.proper_strings = ['PROPER']

        # Cache
        self.cache = tvcache.TVCache(self, min_time=30)

    def login(self):
        if any(dict_from_cookiejar(self.session.cookies).values()):
            return True

        login_params = {
            'username': self.username,
            'password': self.password,
        }

        response = self.get_url(self.urls['login'], post_data=login_params, returns='text')
        if not response:
            logger.warning('Unable to connect to provider')
            return False

        if not re.search('torrents.php', response):
            logger.warning('Invalid username or password. Check your settings')
            return False

        return True

    def search(self, search_strings, age=0, ep_obj=None):
        results = []
        if not self.login():
            return results

        # Search Params
        search_params = {
            'cat[]': ['TV|SD|VOSTFR', 'TV|HD|VOSTFR', 'TV|SD|VF', 'TV|HD|VF', 'TV|PACK|FR', 'TV|PACK|VOSTFR', 'TV|EMISSIONS', 'ANIME'],
            # Both ASC and DESC are available for sort direction
            'way': 'DESC'
        }

        # Units
        units = ['O', 'KO', 'MO', 'GO', 'TO', 'PO']

        for mode in search_strings:
            items = []
            logger.debug('Search Mode: {0}'.format(mode))

            for search_string in search_strings[mode]:

                if mode != 'RSS':
                    logger.debug('Search string: {0}'.format
                                 (search_string))

                # Sorting: Available parameters: ReleaseName, Seeders, Leechers, Snatched, Size
                search_params['order'] = ('Seeders', 'Time')[mode == 'RSS']
                search_params['search'] = re.sub(r'[()]', '', search_string)
                data = self.get_url(self.urls['search'], params=search_params, returns='text')
                if not data:
                    continue

                with BS4Parser(data, 'html5lib') as html:
                    torrent_table = html.find(class_='torrent_table')
                    torrent_rows = torrent_table('tr') if torrent_table else []

                    # Continue only if at least one Release is found
                    if len(torrent_rows) < 2:
                        logger.debug('Data returned from provider does not contain any torrents')
                        continue

                    # Catégorie, Release, Date, DL, Size, C, S, L
                    labels = [label.get_text(strip=True) for label in torrent_rows[0]('td')]

                    # Skip column headers
                    for result in torrent_rows[1:]:
                        cells = result('td')
                        if len(cells) < len(labels):
                            continue

                        try:
                            title = cells[labels.index('Release')].get_text(strip=True)
                            download_url = urljoin(self.url, cells[labels.index('DL')].find('a', class_='tooltip')['href'])
                            if not all([title, download_url]):
                                continue

                            seeders = try_int(cells[labels.index('S')].get_text(strip=True))
                            leechers = try_int(cells[labels.index('L')].get_text(strip=True))

                            # Filter unseeded torrent
                            if seeders < self.minseed or leechers < self.minleech:
                                if mode != 'RSS':
                                    logger.debug('Discarding torrent because it doesn\'t meet the minimum seeders or leechers: {0} (S:{1} L:{2})'.format
                                                 (title, seeders, leechers))
                                continue

                            size_index = labels.index('Size') if 'Size' in labels else labels.index('Taille')
                            torrent_size = cells[size_index].get_text()
                            size = convert_size(torrent_size, units=units) or -1

                            item = {'title': title, 'link': download_url, 'size': size, 'seeders': seeders, 'leechers': leechers, 'hash': ''}
                            if mode != 'RSS':
                                logger.debug('Found result: {0} with {1} seeders and {2} leechers'.format(title, seeders, leechers))

                            items.append(item)
                        except Exception:
                            continue

            # For each search mode sort all the items by seeders if available
            items.sort(key=lambda d: try_int(d.get('seeders', 0)), reverse=True)
            results += items

        return results
