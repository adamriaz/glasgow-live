import json


class RSSEntry(object):

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

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
