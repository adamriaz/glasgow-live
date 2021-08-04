import feedparser

from social_medias import FACEBOOK_PAGE
from models import RSSEntry
from facebook_scraper import get_posts


class FacebookFeedAdapter:

    def get_data(self, pages: int = 3):
        posts = []
        for post in get_posts(account=FACEBOOK_PAGE, pages=pages):
            posts.append(post)
        return posts


class RSSFeedAdapter:

    def __init__(self):
        self.__feedparser = feedparser

    def __get_entries(self, url: str) -> any:
        return self.__feedparser.parse(url)["entries"]

    # TODO GET CHANNEL INFO
    def __get_channel_info(self):
        pass

    def get_RSS_data(self, url: str) -> list[RSSEntry]:
        """
        Iterates through the results to fields that are expected.

        :param url: RSS url string
        :return: Entry list results
        """
        entries = self.__get_entries(url=url)
        entries_data: list[RSSEntry] = []
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
            entries_data.append(entry)

        return entries_data
