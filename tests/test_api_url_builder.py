import unittest

from xcodestream.connection import Connection
from xcodestream.url_api_builder import EndpointEnum, Url_api_builder


class Test_url_api_builder(unittest.TestCase):
    def test_url_api_builder_auth(self):
        url = "https://test.com:5609?username=test&password=pass"
        matched, conn = Connection.from_url(url)
        url = Url_api_builder.build(EndpointEnum.AUTH, conn)
        expected = "https://test.com:5609/player_api.php?username=test&password=pass"
        self.assertEqual(expected, url)

    def test_url_api_builder_user_panel(self):
        url = "https://test.com:5609?username=test&password=pass"
        matched, conn = Connection.from_url(url)
        url = Url_api_builder.build(EndpointEnum.USER_PANEL, conn)
        expected = "https://test.com:5609/panel_api.php?username=test&password=pass"
        self.assertEqual(expected, url)

    def test_url_api_builder_xmltv(self):
        url = "https://test.com:5609?username=test&password=pass"
        matched, conn = Connection.from_url(url)
        url = Url_api_builder.build(EndpointEnum.XMLTV, conn)
        expected = "https://test.com:5609/xmltv.php?username=test&password=pass"
        self.assertEqual(expected, url)

    def test_url_api_builder_live_streams_by_cat(self):
        url = "https://test.com:5609?username=test&password=pass"
        matched, conn = Connection.from_url(url)
        cat = 69
        url = Url_api_builder.build(EndpointEnum.LIVE_STREAMS_BY_CATEGORY, conn, cat)
        expected = f"https://test.com:5609/player_api.php?username=test&password=pass&action=get_live_streams&category_id={cat}"
        self.assertEqual(expected, url)

    def test_url_api_builder_live_streams(self):
        url = "https://test.com:5609?username=test&password=pass"
        matched, conn = Connection.from_url(url)
        url = Url_api_builder.build(EndpointEnum.LIVE_STREAMS, conn)
        expected = f"https://test.com:5609/player_api.php?username=test&password=pass&action=get_live_streams"
        self.assertEqual(expected, url)


if __name__ == "__main__":
    unittest.main()
