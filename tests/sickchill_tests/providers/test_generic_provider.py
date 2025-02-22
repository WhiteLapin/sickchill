"""
Test GenericProvider
"""

import unittest

from mock import MagicMock, patch

from sickchill.providers.GenericProvider import GenericProvider


class GenericProviderTests(unittest.TestCase):
    """
    Test GenericProvider
    """

    def test_get_id(self):
        """
        Test get_id
        """
        test_cases = {
            None: "",
            123: "123",
            12.3: "12_3",
            0: "",
            -123: "_123",
            -12.3: "_12_3",
            "": "",
            " ": "",
            "123": "123",
            " 123 ": "123",
            "12.3": "12_3",
            " 12.3 ": "12_3",
            "0": "0",
            " 0 ": "0",
            "-123": "_123",
            " -123 ": "_123",
            "-12.3": "_12_3",
            " -12.3 ": "_12_3",
            "abc": "abc",
            " abc ": "abc",
            "ABC": "abc",
            " ABC ": "abc",
            ".def": "_def",
            "g,hi": "g_hi",
            "jk!l": "jk_l",
            "mno?": "mno_",
            "_pqr$": "_pqr_",
        }

        unicode_test_cases = {
            "": "",
            " ": "",
            "123": "123",
            " 123 ": "123",
            "12.3": "12_3",
            " 12.3 ": "12_3",
            "0": "0",
            " 0 ": "0",
            "-123": "_123",
            " -123 ": "_123",
            "-12.3": "_12_3",
            " -12.3 ": "_12_3",
            "abc": "abc",
            " abc ": "abc",
            "ABC": "abc",
            " ABC ": "abc",
            ".def": "_def",
            "g,hi": "g_hi",
            "jk!l": "jk_l",
            "mno?": "mno_",
            "_pqr$": "_pqr_",
        }

        for test in test_cases, unicode_test_cases:
            for (name, result) in test.items():
                assert GenericProvider(name).get_id() == result

    def test_image_name(self):
        """
        Test image_name
        """
        test_cases = {
            None: ".png",
            123: "123.png",
            12.3: "12_3.png",
            0: ".png",
            -123: "_123.png",
            -12.3: "_12_3.png",
            "": ".png",
            " ": ".png",
            "123": "123.png",
            " 123 ": "123.png",
            "12.3": "12_3.png",
            " 12.3 ": "12_3.png",
            "0": "0.png",
            " 0 ": "0.png",
            "-123": "_123.png",
            " -123 ": "_123.png",
            "-12.3": "_12_3.png",
            " -12.3 ": "_12_3.png",
            "abc": "abc.png",
            " abc ": "abc.png",
            "ABC": "abc.png",
            " ABC ": "abc.png",
            ".def": "_def.png",
            "g,hi": "g_hi.png",
            "jk!l": "jk_l.png",
            "mno?": "mno_.png",
            "_pqr$": "_pqr_.png",
        }

        unicode_test_cases = {
            "": ".png",
            " ": ".png",
            "123": "123.png",
            " 123 ": "123.png",
            "12.3": "12_3.png",
            " 12.3 ": "12_3.png",
            "0": "0.png",
            " 0 ": "0.png",
            "-123": "_123.png",
            " -123 ": "_123.png",
            "-12.3": "_12_3.png",
            " -12.3 ": "_12_3.png",
            "abc": "abc.png",
            " abc ": "abc.png",
            "ABC": "abc.png",
            " ABC ": "abc.png",
            ".def": "_def.png",
            "g,hi": "g_hi.png",
            "jk!l": "jk_l.png",
            "mno?": "mno_.png",
            "_pqr$": "_pqr_.png",
        }

        for test in test_cases, unicode_test_cases:
            for (name, result) in test.items():
                assert GenericProvider(name).image_name() == result

    def test_is_active(self):
        """
        Test is_active
        """
        assert not GenericProvider("Test Provider").is_active

    def test_is_enabled(self):
        """
        Test is_enabled
        """
        assert not GenericProvider("Test Provider").is_enabled

    def test_make_id(self):
        """
        Test make_id
        """
        test_cases = {
            None: "",
            123: "123",
            12.3: "12_3",
            0: "",
            -123: "_123",
            -12.3: "_12_3",
            "": "",
            " ": "",
            "123": "123",
            " 123 ": "123",
            "12.3": "12_3",
            " 12.3 ": "12_3",
            "0": "0",
            " 0 ": "0",
            "-123": "_123",
            " -123 ": "_123",
            "-12.3": "_12_3",
            " -12.3 ": "_12_3",
            "abc": "abc",
            " abc ": "abc",
            "ABC": "abc",
            " ABC ": "abc",
            ".def": "_def",
            "g,hi": "g_hi",
            "jk!l": "jk_l",
            "mno?": "mno_",
            "_pqr$": "_pqr_",
        }

        unicode_test_cases = {
            "": "",
            " ": "",
            "123": "123",
            " 123 ": "123",
            "12.3": "12_3",
            " 12.3 ": "12_3",
            "0": "0",
            " 0 ": "0",
            "-123": "_123",
            " -123 ": "_123",
            "-12.3": "_12_3",
            " -12.3 ": "_12_3",
            "abc": "abc",
            " abc ": "abc",
            "ABC": "abc",
            " ABC ": "abc",
            ".def": "_def",
            "g,hi": "g_hi",
            "jk!l": "jk_l",
            "mno?": "mno_",
            "_pqr$": "_pqr_",
        }

        for test in test_cases, unicode_test_cases:
            for (name, result) in test.items():
                assert GenericProvider.make_id(name) == result

    def test_seed_ratio(self):
        """
        Test seed_ratio
        """
        assert GenericProvider("Test Provider").seed_ratio() == ""

    def test__check_auth(self):
        """
        Test _check_auth
        """
        assert GenericProvider("Test Provider")._check_auth()

    def test_login(self):
        """
        Test login
        """
        assert GenericProvider("Test Provider").login()

    def test_search(self):
        """
        Test search
        """
        test_cases = {
            None: [],
            123: [],
            12.3: [],
            -123: [],
            -12.3: [],
            "": [],
            "123": [],
            "12.3": [],
            "-123": [],
            "-12.3": [],
        }

        unicode_test_cases = {
            "": [],
            "123": [],
            "12.3": [],
            "-123": [],
            "-12.3": [],
        }

        for test in test_cases, unicode_test_cases:
            for (search_params, result) in test.items():
                assert GenericProvider("Test Provider").search(search_params) == result

    def test__get_size(self):
        """
        Test _get_size
        """
        assert GenericProvider("Test Provider")._get_size(None) == -1

    def test__get_storage_dir(self):
        """
        Test _get_storage_dir
        """
        assert GenericProvider("Test Provider")._get_storage_dir() == ""

    def test__get_title_and_url(self):
        """
        Test _get_title_and_url
        """
        items_list = [
            None,
            {},
            {"link": None, "title": None},
            {"link": "", "title": ""},
            {"link": "http://www.google.com/&amp;foo=bar%26tr%3Dtest", "title": "Some Title"},
        ]
        results_list = [("", ""), ("", ""), ("", ""), ("", ""), ("Some.Title", "http://www.google.com/&foo=bar&tr=test")]

        unicode_items_list = [{"link": "", "title": ""}, {"link": "http://www.google.com/&amp;foo=bar%26tr%3Dtest", "title": "Some Title"}]
        unicode_results_list = [("", ""), ("Some.Title", "http://www.google.com/&foo=bar&tr=test")]

        assert len(items_list) == len(results_list), "Number of parameters ({0:d}) and results ({1:d}) does not match".format(
            len(items_list), len(results_list)
        )

        assert len(unicode_items_list) == len(unicode_results_list), "Number of parameters ({0:d}) and results ({1:d}) does not match".format(
            len(unicode_items_list), len(unicode_results_list)
        )

        for (index, item) in enumerate(items_list):
            assert GenericProvider("Test Provider")._get_title_and_url(item) == results_list[index]

        for (index, item) in enumerate(unicode_items_list):
            assert GenericProvider("Test Provider")._get_title_and_url(item) == unicode_results_list[index]

    def test__verify_download(self):
        """
        Test _verify_download
        """
        assert GenericProvider("Test Provider")._verify_download("Random.torrent")

    @patch("sickchill.providers.GenericProvider.download_file")
    @patch("sickchill.providers.GenericProvider.remove_file_failed")
    def test_download_file(self, remove_file_mock, df_mock):
        """
        Test download_result
        """
        domain = "domain"
        filename = "TestFilename.nzb"
        urls = [
            "http://{0}/{1}.torrentNO_DOWNLOAD_NAME".format(domain, filename),
            "http://{0}/{1}.torrent".format(domain, filename),
        ]

        # Test the login() check
        gp1 = GenericProvider("Test Provider 1")
        login_mock = MagicMock()
        login_mock.return_value = False
        with patch.object(gp1, "login", login_mock):
            assert not gp1.download_result("result 1")
            assert login_mock.called

        # Test the _make_url call
        gp2 = GenericProvider("Test Provider 2")
        make_url_mock = MagicMock()
        make_url_mock.return_value = (urls, filename)
        df_mock.return_value = True
        with patch.object(gp2, "_make_url", make_url_mock):
            resp = gp2.download_result("result 2")
            assert resp
            assert "Referer" in gp2.headers
            assert domain in gp2.headers["Referer"]
            assert df_mock.called

        # Test the remove_file_failed path
        gp3 = GenericProvider("Test Provider 3")
        make_url_mock = MagicMock()
        make_url_mock.return_value = (urls, filename)
        verify_download_mock = MagicMock()
        verify_download_mock.return_value = False
        df_mock.return_value = True
        with patch.object(gp3, "_make_url", make_url_mock):
            with patch.object(gp3, "_verify_download", verify_download_mock):
                resp = gp3.download_result("result 3")
                assert not resp
                assert remove_file_mock.called


if __name__ == "__main__":
    print("=====> Testing {0}".format(__file__))

    SUITE = unittest.TestLoader().loadTestsFromTestCase(GenericProviderTests)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
