import unittest

from glasgow_live.models import RSSEntry


class TestAdapter(unittest.TestCase):

    def setUp(self):
        self.entry = RSSEntry(
            title="test",
            link="test",
            id="test",
            summary="test",
            published="test",
            author="test",
            media_keywords="test test",
            media_image="test"
        )

    def test_adapter(self):
        pass
