from dataclasses import dataclass
from typing import List
from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB

from app.api.model.album import Album
from app.api.model.artist import Artist
from app.api.model.external_urls import ExternalUrls
from app.api.model.item import Item
from app.api.model.track import Track
from app.model import Base


@dataclass
class Welcome(Base):
    # user_id = Column(Integer, primary_key=True)
    # username = Column(String(20), nullable=False)
    # email = Column(String(320), unique=True, nullable=False)
    # password = Column(String(80), nullable=False)
    # info = Column(JSONB, nullable=True)
    # token = Column(String(255), nullable=False)
    id = Column(Integer, primary_key=True)
    href = Column(String, nullable=True)
    items: List[Item]
    limit: int
    next: str
    offset: int
    previous: None
    total: int

    def __init__(self, json):
        self.href = json['href']
        self.items = self.create_items(json['items'])
        self.limit = json['limit']
        self.next = json['next']
        self.offset = json['offset']
        self.previous = json['previous']
        self.total = json['total']

    def create_items(self, items: dict):
        list = []
        for item in items:
            i = Item(added_at=item['added_at'], track=self.create_track(item['track']))
            list.append(i)

        return list

    def create_track(self, json):
        album_data = json['album']

        # TODO popular external_ids
        # TODO Construir images
        track = Track(album=self.create_album(album_data), artists=self.create_artists(json['artists']), available_markets=json['available_markets'], disc_number=json['disc_number'], durations_ms=json['duration_ms'], explicit=json['explicit'],
                      external_urls=self.create_external_urls(json['external_urls']), external_ids=None, href=json['href'], id= json['id'], is_local=json['is_local'],
                      name=json['name'], popularity=json['popularity'], preview_url=json['preview_url'], track_number=json['track_number'], type=json['type'], uri=json['uri'])
        return track

    def create_images(self, json):
        return None

    def create_album(self, album_data):
        album = Album(album_type=album_data['album_type'], artists=self.create_artists(album_data['artists']),
                      available_markets=album_data['available_markets'],
                      external_urls=self.create_external_urls(album_data['external_urls']), href=album_data['href'],
                      id=album_data['id'], images=self.create_images(album_data['images']), name=album_data['name'],
                      release_date=album_data['release_date'],
                      release_date_precision=album_data['release_date_precision'],
                      total_tracks=album_data['total_tracks'],
                      type=album_data['type'], uri=album_data['uri'])
        return album

    def create_artists(self, json):
        list =[]
        for i in json:
            artist = Artist(external_urls=self.create_external_urls(json=i['external_urls']), href=i['href'], id=i['id'], name=i['name'], type=i['type'], uri=i['uri'])
            list.append(artist)
        return list

    @staticmethod
    def create_external_urls(json):
        list = []
        url = ExternalUrls(spotify_url=json['spotify'])
        list.append(url)
        return list

    FIELDS = {
        'href': str
    }

    FIELDS.update(Base.FIELDS)

