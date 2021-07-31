import json


class Entry(object):

    def __init__(self, title: str, link: str, id: str, summary: str, published: str, author: str, media_keywords: str,
                 media_image: str):
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
