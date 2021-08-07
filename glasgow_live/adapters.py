import feedparser
import facebook_scraper
import twint
from typing import Any, Iterator
from social_medias import FACEBOOK_PAGE, TWITTER_PAGE
from models import RSSEntry, FacebookPost


class TwitterFeedAdapter:

    def __init__(self):
        self.twint = twint
        self.twitter = self.twint.Config()
        self.twitter.Hide_output = True

    def __get_tweets(self, pages: int = 1) -> list:
        try:
            posts = []
            self.twitter.Username = TWITTER_PAGE
            self.twitter.Limit = pages
            self.twitter.Store_json = True
            self.twitter.Store_object = True
            self.twitter.Store_object_tweets_list = posts
            self.twint.run.Search(self.twitter)
            return posts
        except Exception as e:
            raise ValueError(f"Error occurred on Twitter Feed. {e}")

    def get_data(self, pages: int = 1) -> list[dict[str, Any]]:
        tweets = []
        tweets_fetched = self.__get_tweets(pages)
        # TODO ADD MODEL
        for i in tweets_fetched:
            tweets.append(i.__dict__)

        return tweets


class FacebookFeedAdapter:

    def __init__(self):
        self.facebook_scraper = facebook_scraper

    def __get_posts(self, pages: int = 3) -> Iterator[dict[str, Any]]:
        try:
            return self.facebook_scraper.get_posts(account=FACEBOOK_PAGE, pages=pages)
        except Exception as e:
            raise ValueError(f"Error occurred on Facebook Feed. {e}")

    def get_data(self, pages: int = 3) -> list[dict[str, Any]]:
        """
        Iterates the results from Facebook page.

        :param pages: Limit number of facebook pages
        :return: FacebookPost results
        """
        posts = []
        for item in self.__get_posts(pages):
            post = FacebookPost(
                post_id=item["post_id"],
                text=item["text"],
                post_text=item["post_text"],
                shared_text=item["shared_text"],
                time=item["time"],
                image=item["image"],
                image_lowquality=item["image_lowquality"],
                images=item["images"],
                images_description=item["images_description"],
                images_lowquality=item["images_lowquality"],
                images_lowquality_description=item["images_lowquality_description"],
                video=item["video"],
                video_duration_seconds=item["video_duration_seconds"],
                video_height=item["video_height"],
                video_id=item["video_id"],
                video_quality=item["video_quality"],
                video_size_mb=item["video_size_MB"],
                video_thumbnail=item["video_thumbnail"],
                video_watches=item["video_watches"],
                video_width=item["video_width"],
                likes=item["likes"],
                comments=item["comments"],
                shares=item["shares"],
                post_url=item["post_url"],
                link=item["link"],
                user_id=item["user_id"],
                username=item["username"],
                user_url=item["user_url"],
                is_live=item["is_live"],
            )
            posts.append(post.__dict__)
        return posts


class RSSFeedAdapter:

    def __init__(self):
        self.__feedparser = feedparser

    def __get_entries(self, url: str) -> any:
        try:
            return self.__feedparser.parse(url)["entries"]
        except Exception as e:
            raise ValueError(f"Error occurred on RSS Feed. {e}")

    # TODO GET CHANNEL INFO
    def __get_channel_info(self):
        pass

    def get_rss_data(self, url: str) -> list[dict[str, Any]]:
        """
        Iterates the results from RSS url.

        :param url: RSS url
        :return: RSSEntry results
        """
        entries = self.__get_entries(url=url)
        entries_data = []
        for item in entries:
            entry = RSSEntry(
                title=item["title"],
                link=item["link"],
                id=item["id"],
                summary=item["summary"],
                published=item["published"],
                author=item["author"],
                media_keywords=item["media_keywords"],
                media_image=item["media_content"][0]["url"] if len(item["media_content"]) > 0 else None
            )
            entries_data.append(entry.__dict__)

        return entries_data
