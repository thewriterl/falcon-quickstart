from dataclasses import dataclass
from typing import List
from datetime import datetime

from app.api.model.artist import Artist
from app.api.model.external_urls import ExternalUrls
from app.api.model.image import Image

@dataclass
class Album(object):
    album_type: str
    artists: List[Artist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: datetime
    release_date_precision: str
    total_tracks: int
    type: str
    uri: str

    def __init__(self, album_type, artists, available_markets, external_urls, href, id, images, name, release_date, release_date_precision, total_tracks, type, uri):
        self.album_type = album_type
        self.artists = artists
        self.available_markets = available_markets
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.total_tracks = total_tracks
        self.type = type
        self.uri = uri
