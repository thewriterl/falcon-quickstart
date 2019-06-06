from dataclasses import dataclass
from typing import List
from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

from app.api.model.artist import Artist
from app.api.model.external_urls import ExternalUrls
from app.api.model.image import Image
from app.model import Base


@dataclass
class Album(Base):
    id = Column(Integer, primary_key=True)
    album_type = Column(String, nullable=True)
    artists = Column(Integer, ForeignKey("artist.id"))
    available_markets = Column(String, nullable=False)
    external_urls_id = Column(Integer, ForeignKey("external_url.id"))
    href = Column(String, nullable=False)
    spotify_id = Column(String, nullable=False)
    images = Column(Integer, ForeignKey("image.id"))
    name = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)
    release_date_precision = Column(String, nullable=True)
    total_tracks = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    uri = Column(String, nullable=False)

    # album_type: str
    # artists: List[Artist]
    # available_markets: List[str]
    # external_urls: ExternalUrls
    # href: str
    # id: str
    # images: List[Image]
    # name: str
    # release_date: datetime
    # release_date_precision: str
    # total_tracks: int
    # type: str
    # uri: str

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
