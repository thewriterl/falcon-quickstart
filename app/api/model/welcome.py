from dataclasses import dataclass
from typing import List
from datetime import datetime

from app.api.model.item import Item


@dataclass
class Welcome(object):
    href: str
    items: List[Item]
    limit: int
    next: str
    offset: int
    previous: None
    total: int

    def __init__(self, json):
        self.href = json['href']
        self.items = self.create_items(json['items'])


    @staticmethod
    def create_items(items: dict):
        for item in items['items']:
            i = Item(added_at=item['added_at'], track=)

    @staticmethod
    def create_track():