import requests


class Client(object):
    def __init__(self, url: str):
        self._url = url

    def user_panel(self):
        r = requests.get(self._url)

    def auth(self):
        r = requests.get(self._url)

    def live_streams(self):
        ...

    def vods(self):
        ...

    def live_categories(self):
        ...

    def live_streams_by_category(self, category: str):
        ...

    def series(self):
        ...

    def xmltv(self):
        ...

    def all_epg(self):
        ...

    def short_epg(self):
        ...

    def catchup(self):
        ...
