import os
import unittest
from xcodestream.client import Client


class Test_Client(unittest.TestCase):
    def test_auth(self):
        url = os.environ.get("PLAYLIST_URL_TEST")
        client = Client(url)
        res = client.auth()
        self.assertIsNotNone(res)
        self.assertIsNotNone(res["user_info"])
        self.assertIsNotNone(res["server_info"])

    def test_live_streams(self):
        url = os.environ.get("PLAYLIST_URL_TEST")
        client = Client(url)
        res = client.live_streams()
        self.assertIsNotNone(res)
        self.assertTrue(len(res) > 0)

    def test_live_streams_by_category(self):
        url = os.environ.get("PLAYLIST_URL_TEST")
        client = Client(url)
        res = client.live_streams_by_category(3)
        self.assertIsNotNone(res)
        self.assertTrue(len(res) > 0)


if __name__ == "__main__":
    unittest.main()
