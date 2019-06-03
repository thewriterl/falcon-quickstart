from dataclasses import dataclass

@dataclass
class ExternalIDS(object):
    isrc: str

    def __init__(self, isrc):
        self.isrc = isrc