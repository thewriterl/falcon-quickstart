from dataclasses import dataclass


@dataclass
class ExternalUrls(object):
    spotify: str

    def __init__(self, spotify_url):
        self.spotify = spotify_url