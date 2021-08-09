from typing import Any

from adapters import RSSFeedAdapter, FacebookFeedAdapter, TwitterFeedAdapter
import rss_links


def rss_feed(url: str) -> list[dict[str, Any]]:
    return RSSFeedAdapter().get_rss_data(url)


def facebook_feed(pages: int = 3) -> list[dict[str, Any]]:
    return FacebookFeedAdapter().get_data(pages=pages)


def twitter_feed(pages: int = 1) -> list[dict[str, Any]]:
    return TwitterFeedAdapter().get_data(pages=pages)


if __name__ == "__main__":
    data = twitter_feed()

    print(data)
