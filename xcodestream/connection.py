import re
from idlelib import query
from urllib.parse import urlparse

class connection:
    def __init__(
        self,
        scheme: str = "http",
        server: str = "",
        port: str = 80,
        username: str = "",
        password: str = "",
    ):
        self.scheme = scheme
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.__class__} {self.scheme}://{self.server}:{self.port}?username={self.username}&password={self.password}"

    def __str__(self):
        port = f":{self.port}" if self.port else ""
        return (
            f"{self.scheme}://{self.server}{port}?username={self.username}&password={self.password}"
        )

    @classmethod
    def from_url(cls, url: str):
        o = urlparse(url)
        regexp_url = "^username=(?P<username>\w+)&password=(?P<password>\w+)"
        res = re.match(regexp_url, o.query, re.IGNORECASE)
        return (
            (True, cls(server=o.hostname, port=o.port, scheme=o.scheme, **res.groupdict()))
            if res
            else (False, cls())
        )
