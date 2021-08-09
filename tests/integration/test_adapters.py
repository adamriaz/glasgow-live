from typing import Iterator

from glasgow_live.adapters import TwitterFeedAdapter, FacebookFeedAdapter, RSSFeedAdapter
import unittest

from glasgow_live.rss_links import GLASGOW_NEWS


class TestTwitterFeedAdapter(unittest.TestCase):

    def setUp(self):
        self.twitter_adapter = TwitterFeedAdapter()

    def test__get_data(self):
        test = self.twitter_adapter._get_tweets()
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")

    def test_get_data(self):
        test = self.twitter_adapter.get_data()
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")


class TestFacebookFeedAdapter(unittest.TestCase):

    def setUp(self):
        self.facebook_adapter = FacebookFeedAdapter()

    def test__get_posts(self):
        test = self.facebook_adapter._get_posts(1)
        self.assertIsInstance(test, Iterator, msg="Expects to be an Iterator/Generator")

    def test_get_data(self):
        test = self.facebook_adapter.get_data()
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")


class TestRSSFeedAdapter(unittest.TestCase):

    def setUp(self):
        self.rss_adapter = RSSFeedAdapter()

    def test__get_entries(self):
        test = self.rss_adapter._get_entries(GLASGOW_NEWS)
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")

    def test_get_rss_data(self):
        test = self.rss_adapter.get_rss_data(GLASGOW_NEWS)
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")

