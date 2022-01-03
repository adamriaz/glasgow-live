from adapters import RSSFeedAdapter


def rss_feed(url: str) -> list:
    """
    Returns the results from RSS url.

    :param url: RSS url
    :return: RSS list
    """
    return RSSFeedAdapter(url).get_rss_data()
