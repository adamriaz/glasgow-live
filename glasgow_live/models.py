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


class FacebookPost:

    def __init__(
            self,
            post_id: str = None,
            text: str = None,
            post_text: str = None,
            shared_text: str = None,
            time: datetime = None,
            image: str = None,
            image_lowquality: str = None,
            images: list = None,
            images_description: list = None,
            images_lowquality: list = None,
            images_lowquality_description: list = None,
            video: str = None,
            video_duration_seconds: int = None,
            video_height: int = None,
            video_id: str = None,
            video_quality: str = None,
            video_size_MB: float = None,
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
        self.video_size_MB = video_size_MB
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


class TwitterTweet:

    def __init__(
            self,
            id: int = None,
            id_str: str = None,
            conversation_id: str = None,
            datetime: str = None,
            datestamp: str = None,
            timestamp: str = None,
            user_id: int = None,
            user_id_str: str = None,
            username: str = None,
            name: str = None,
            place: str = None,
            timezone: str = None,
            mentions: list = None,
            reply_to: list = None,
            urls: list = None,
            video: int = None,
            thumbnail: str = None,
            tweet: str = None,
            lang: str = None,
            hashtags: list = None,
            cashtags: list = None,
            replies_count: int = None,
            retweets_count: int = None,
            likes_count: int = None,
            link: str = None,
            retweet: bool = False,
            retweet_id: str = None,
            retweet_date: str = None,
            user_rt: str = None,
            user_rt_id: str = None,
            quote_url: str = None,
            near: str = None,
            geo: str = None,
            source: str = None,
            translate: str = None,
            trans_src: str = None,
            trans_dest: str = None
    ):
        self.id = id
        self.id_str = id_str
        self.conversation_id = conversation_id
        self.datetime = datetime
        self.datestamp = datestamp
        self.timestamp = timestamp
        self.user_id = user_id
        self.user_id_str = user_id_str
        self.username = username
        self.name = name
        self.place = place
        self.timezone = timezone
        self.mentions = mentions
        self.reply_to = reply_to
        self.urls = urls
        self.video = video
        self.thumbnail = thumbnail
        self.tweet = tweet
        self.lang = lang
        self.hashtags = hashtags
        self.cashtags = cashtags
        self.replies_count = replies_count
        self.retweets_count = retweets_count
        self.likes_count = likes_count
        self.link = link
        self.retweet = retweet
        self.retweet_id = retweet_id
        self.retweet_date = retweet_date
        self.user_rt = user_rt
        self.user_rt_id = user_rt_id
        self.quote_url = quote_url
        self.near = near
        self.geo = geo
        self.source = source
        self.translate = translate
        self.trans_src = trans_src
        self.trans_dest = trans_dest
