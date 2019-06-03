from dataclasses import dataclass

@dataclass
class Image(object):
    height: int
    url: str
    width: int

    def __init__(self, height, url, width):
        self.height = height
        self.url = url
        self.width = width
