from typing import Any

from adapters import RSSFeedAdapter, FacebookFeedAdapter, TwitterFeedAdapter
from glasgow_live.social_medias import TWITTER_PAGE, FACEBOOK_PAGE


def rss_feed(url: str) -> list:
    """
    Returns the results from RSS url.

    :param url: RSS url
    :return: RSS list
    """
    return RSSFeedAdapter(url).get_rss_data()


def facebook_feed(pages: int = 3) -> list:
    """
    Returns the results from facebook page.

    :param pages: Number of pages
    :return: Facebook posts
    """
    return FacebookFeedAdapter(FACEBOOK_PAGE).get_data(pages=pages)


def twitter_feed(pages: int = 1) -> list:
    """
    Returns the results from twitter page.

    :param pages: Number of pages
    :return: Twitter tweets
    """
    return TwitterFeedAdapter(TWITTER_PAGE).get_data(pages=pages)
