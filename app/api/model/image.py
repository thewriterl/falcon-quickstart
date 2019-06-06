from sqlalchemy import Column, Integer, String

from app.model import Base


class Image(Base):
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    url = Column(String, nullable=False)

    def __init__(self, height, url, width):
        self.height = height
        self.url = url
        self.width = width
