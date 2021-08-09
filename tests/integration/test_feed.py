import unittest

from glasgow_live.feed import rss_feed, facebook_feed, twitter_feed
import glasgow_live.rss_links as rss_links


class TestFeed(unittest.TestCase):

    def test_rss_feed(self):
        test = rss_feed(rss_links.GLASGOW_NEWS)
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")

    def test_facebook_feed(self):
        test = facebook_feed()
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")

    def test_twitter_feed(self):
        test = twitter_feed()
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")