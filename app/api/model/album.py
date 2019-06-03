from dataclasses import dataclass
from typing import List
from datetime import datetime

from app.api.model.artist import Artist
from app.api.model.exertnal_urls import ExternalUrls
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
