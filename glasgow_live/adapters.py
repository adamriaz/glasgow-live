from typing import Any, Iterator
import feedparser

from social_medias import FACEBOOK_PAGE
from models import RSSEntry
import facebook_scraper


class FacebookFeedAdapter:

    def __init__(self):
        self.facebook_scraper = facebook_scraper

    def __get_posts(self, pages: int = 3) -> Iterator[dict[str, Any]]:
        try:
            return self.facebook_scraper.get_posts(account=FACEBOOK_PAGE, pages=pages)
        except Exception as e:
            raise ValueError(f"Error occurred on Facebook Feed. {e}")

    def get_data(self, pages: int = 3) -> list[dict[str, Any]]:
        posts = []
        # TODO ADD MODEL
        for post in self.__get_posts(pages):
            posts.append(post)
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
        Iterates through the results to fields that are expected.

        :param url: RSS url
        :return: RSSEntry results
        """
        entries = self.__get_entries(url=url)
        entries_data: list[dict[str, Any]] = []
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
