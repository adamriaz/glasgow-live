import json
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

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


class FacebookPost:

    def __init__(
            self,
            post_id: str,
            text: str = None,
            post_text: str = None,
            shared_text: str = None,
            time: datetime = None,
            image: str = None,
            image_lowquality: str = None,
            images: list[str] = None,
            images_description: list[str] = None,
            images_lowquality: list[str] = None,
            images_lowquality_description: list[str] = None,
            video: str = None,
            video_duration_seconds: int = None,
            video_height: int = None,
            video_id: str = None,
            video_quality: str = None,
            video_size_mb: float = None,
            video_thumbnail: str = None,
            video_watches: int = None,
            video_width: int = None,
            likes: int = None,
            comments: int = None,
            shares: int = None,
            post_url: str = None,
            link: str = None,
            user_id: str = None,
            username: str = None,
            user_url: str = None,
            is_live: bool = False
    ):
        self.post_id = post_id
        self.text = text
        self.post_text = post_text
        self.shared_text = shared_text
        self.time = time
        self.image = image
        self.image_lowquality = image_lowquality
        self.images = images
        self.images_description = images_description
        self.images_lowquality = images_lowquality
        self.images_lowquality_description = images_lowquality_description
        self.video = video
        self.video_duration_seconds = video_duration_seconds
        self.video_height = video_height
        self.video_id = video_id
        self.video_quality = video_quality
        self.video_size_mb = video_size_mb
        self.video_thumbnail = video_thumbnail
        self.video_watches = video_watches
        self.video_width = video_width
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.post_url = post_url
        self.link = link
        self.user_id = user_id
        self.username = username
        self.user_url = user_url
        self.is_live = is_live

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
