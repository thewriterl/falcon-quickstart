from dataclasses import dataclass

@dataclass
class Image(object):
    height: int
    url: str
    width: int
