import feedparser
from models import RSSEntry


class RSSFeedAdapter:

    def __init__(self, url: str):
        self._feedparser = feedparser
        self._url = url

    def _get_entries(self) -> any:
        try:
            return self._feedparser.parse(self._url)["entries"]
        except Exception as e:
            raise ValueError(f"Error occurred on RSS Feed. {e}")

    def get_rss_data(self) -> list:
        """
        Returns the results from RSS url.

        :param url: RSS url
        :return: RSSEntry results
        """
        entries = self._get_entries()
        entries_data = []
        for item in entries:
            entry = RSSEntry(
                title=item["title"] if "title" in item else None,
                link=item["link"] if "link" in item else None,
                id=item["id"] if "id" in item else None,
                summary=item["summary"] if "summary" in item else None,
                published=item["published"] if "published" in item else None,
                author=item["author"] if "author" in item else None,
                media_keywords=item["media_keywords"] if "media_keywords" in item else None,
                media_image=item["media_content"][0]["url"] if "media_content" in item
                                                               and len(item["media_content"]) > 0 else None
            )
            entries_data.append(entry.__dict__)

        return entries_data
