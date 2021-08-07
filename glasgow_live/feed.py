from typing import Any

from adapters import RSSFeedAdapter, FacebookFeedAdapter, TwitterFeedAdapter
from rss_links import LATEST_NEWS, SPORT_NEWS
from models import RSSEntry


def get_news() -> list[dict[str, Any]]:
    return RSSFeedAdapter().get_rss_data(SPORT_NEWS)


def get_facebook_feed():
    return FacebookFeedAdapter().get_data(pages=1)


def get_twitter_feed():
    return TwitterFeedAdapter().get_data(pages=3)


if __name__ == "__main__":
    data = get_twitter_feed()

    print(data)
