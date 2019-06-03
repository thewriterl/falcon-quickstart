from dataclasses import dataclass
from typing import List
from datetime import datetime

from app.api.model.album import Album
from app.api.model.artist import Artist
from app.api.model.exertnal_urls import ExternalUrls
from app.api.model.external_ids import ExternalIDS


@dataclass
class Track(object):
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIDS
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: bool
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: str
    uri: str
