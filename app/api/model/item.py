import datetime

from app.api.model.track import Track


class Item(object):
    added_at: datetime
    track: Track

    def __init__(self, added_at, track):
        self.added_at = added_at
        self.track = track
