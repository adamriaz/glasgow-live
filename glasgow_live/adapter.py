import feedparser

from entry_data import Entry


class FeedAdapter:

    def __init__(self):
        self.__feedparser = feedparser

    def __get_entries(self, url: str):
        return self.__feedparser.parse(url)["entries"]

    def get_data(self, url: str) -> list[Entry]:
        entries = self.__get_entries(url=url)
        entries_data: list[Entry] = []
        for item in entries:
            entry = Entry(
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

