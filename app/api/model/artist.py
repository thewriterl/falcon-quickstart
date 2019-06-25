
from typing import List
from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey,String

from app.api.model.external_urls import ExternalUrls
from app.model import Base


class Artist(Base):
    id = Column(Integer, primary_key=True)
    external_urls_id = Column(Integer, ForeignKey("external_url.id"))
    href = Column(String, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    uri = Column(String, nullable=False)
    # external_urls: ExternalUrls
    # href: str
    # id: str
    # name: str
    # type: str
    # uri: str

    def __init__(self, external_urls, href, id, name, type, uri):
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.name = name
        self.type = type
        self.uri = uri
