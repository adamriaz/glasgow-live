from datetime import datetime


class RSSEntry:

    def __init__(
            self,
            title: str = None,
            link: str = None,
            id: str = None,
            summary: str = None,
            published: str = None,
            author: str = None,
            media_keywords: str = None,
            media_image: str = None):
        self.title = title
        self.link = link
        self.id = id
        self.published = published
        self.summary = summary
        self.author = author
        self.media_keywords = media_keywords
        self.media_image = media_image
