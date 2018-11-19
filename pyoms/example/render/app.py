# coding=utf-8
from core.base import Base
from core.inner import Inner

class News(Base):

    data = [
        {
        "title": "New one",
        "content": "This one news",
        "date": "16.11.2018",
        },
        {
        "title": "New two",
        "content": "This two news",
        "date": "17.11.2018",
        }
    ]

    def created(self):
        Inner().render('.block-news', self.data)

app = News()