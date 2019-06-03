from dataclasses import dataclass
from typing import List
from datetime import datetime

from app.api.model.external_urls import ExternalUrls


@dataclass
class Artist(object):
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str

    def __init__(self, external_urls, href, id, name, type, uri):
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.name = name
        self.type = type
        self.uri = uri
