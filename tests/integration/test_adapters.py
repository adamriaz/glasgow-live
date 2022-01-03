from typing import Iterator

from glasgow_live.adapters import RSSFeedAdapter
import unittest

from glasgow_live.rss_links import GLASGOW_NEWS


class TestRSSFeedAdapter(unittest.TestCase):

    def setUp(self):
        self.rss_adapter = RSSFeedAdapter(GLASGOW_NEWS)

    def test__get_entries(self):
        test = self.rss_adapter._get_entries()
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")

    def test_get_rss_data(self):
        test = self.rss_adapter.get_rss_data()
        self.assertGreater(len(test), 0, msg="Expects list to be greater than 0")

