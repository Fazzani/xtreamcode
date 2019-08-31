import unittest

from xcodestream.connection import Connection


class TestConnection(unittest.TestCase):

    def test_matched_url(self):
        url = "https://test.com:5609?username=test&password=pass"
        matched, conn = Connection.from_url(url)
        self.assertTrue(matched)
        self.assertTrue(isinstance(conn, Connection))
        self.assertEqual(str(conn), url)

    def test_matched_url_without_port(self):
        url = "http://test.com?username=test&password=pass"
        matched, conn = Connection.from_url(url)
        self.assertTrue(matched)
        self.assertTrue(isinstance(conn, Connection))
        self.assertEqual(str(conn), url)

    def test_not_matched_username_url(self):
        url = "https://test.com:5609?usename=test&password=pass"
        matched, conn = Connection.from_url(url)
        self.assertFalse(matched)

    # def test_parse(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
