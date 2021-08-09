from typing import Any

from adapters import RSSFeedAdapter, FacebookFeedAdapter, TwitterFeedAdapter
import glasgow_live.rss_links as rss_links

def rss_feed(url: str) -> list[dict[str, Any]]:
    """
    Returns the results from RSS url.

    :param url: RSS url
    :return: RSS list
    """
    return RSSFeedAdapter().get_rss_data(url)


def facebook_feed(pages: int = 3) -> list[dict[str, Any]]:
    """
    Returns the results from facebook page.

    :param pages: Number of pages
    :return: Facebook posts
    """
    return FacebookFeedAdapter().get_data(pages=pages)


def twitter_feed(pages: int = 1) -> list[dict[str, Any]]:
    """
    Returns the results from twitter page.

    :param pages: Number of pages
    :return: Twitter tweets
    """
    return TwitterFeedAdapter().get_data(pages=pages)



