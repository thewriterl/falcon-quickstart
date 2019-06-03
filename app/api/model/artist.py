from dataclasses import dataclass
from typing import List
from datetime import datetime

from app.api.model.exertnal_urls import ExternalUrls


@dataclass
class Artist(object):
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str
