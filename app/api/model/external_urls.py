

from sqlalchemy import Column, Integer, String

from app.model import Base


class ExternalUrls(Base):
    __tablename__ = 'external_url'
    id = Column(Integer, primary_key=True)
    spotify = Column(String, nullable=False)

    def __init__(self, spotify_url):
        self.spotify = spotify_url

