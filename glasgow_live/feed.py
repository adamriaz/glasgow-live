from adapters import RSSFeedAdapter, FacebookFeedAdapter
from rss_links import LATEST_NEWS, SPORT_NEWS
from models import RSSEntry


def get_news() -> list[RSSEntry]:
    return RSSFeedAdapter().get_RSS_data(SPORT_NEWS)


def get_facebook_feed():
    return FacebookFeedAdapter().get_data(pages=3)


if __name__ == "__main__":
    data = get_facebook_feed()
    print(data)