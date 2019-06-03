import datetime
from dataclasses import dataclass

from app.api.model.track import Track


@dataclass
class Item(object):
    added_at: datetime
    track: Track

    def __init__(self, added_at, track):
        self.added_at = added_at
        self.track = track
