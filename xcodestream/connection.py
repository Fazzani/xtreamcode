class connection(object):

    def __init__(self, url: str):
        self.server = ""
        self.username = ""
        self.password = ""

    def __init__(self, server: str, username: str, password: str):
        self.server = server
        self.username = username
        self.password = password

    @staticmethod
    def parseUrl(url: str) -> connection:
        return connection(url)
