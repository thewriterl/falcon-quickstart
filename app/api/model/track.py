
from typing import List
from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.api.model.album import Album
from app.api.model.artist import Artist
from app.api.model.external_urls import ExternalUrls
from app.api.model.external_ids import ExternalIDS
from app.model import Base



class Track(Base):
    # billing_address_id = Column(Integer, ForeignKey("address.id"))
    # shipping_address_id = Column(Integer, ForeignKey("address.id"))
    #
    # billing_address = relationship("Address", foreign_keys=[billing_address_id])
    # shipping_address = relationship("Address", foreign_keys=[shipping_address_id])

    album_id = Column(Integer, ForeignKey("album.id"))
    artists_id = Column(Integer, ForeignKey("artist.id"))
    available_markets = Column(String, nullable=False)
    disc_number = Column(Integer, nullable=True)
    duration_ms = Column(Integer, nullable=False)
    explicit = Column(Boolean, nullable=False)
    href = Column(String, nullable=False)
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    popularity = Column(Integer, nullable=False)
    preview_url = Column(String, nullable=False)
    track_number = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    uri = Column(String, nullable=False)
    # album: Album
    # artists: List[Artist]
    # available_markets: List[str]
    # disc_number: int
    # duration_ms: int
    # explicit: bool
    external_ids: ExternalIDS
    external_urls: ExternalUrls
    # href: str
    # id: str
    is_local: bool
    # name: str
    # popularity: int
    # preview_url: str
    # track_number: int
    # type: str
    # uri: str

    def __init__(self, album, artists, available_markets, disc_number, durations_ms, explicit, external_ids, external_urls, href, id, is_local, name, popularity, preview_url, track_number, type, uri):
        self.album_id = album
        self.artists_id = artists
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = durations_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.is_local = is_local
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri

    FIELDS = {
        'album_id': [int],
        'artists_id': [int],
        'available_markets': str,
        'disc_number': int
    }


    FIELDS.update(Base.FIELDS)

