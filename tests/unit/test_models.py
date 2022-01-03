import datetime
import unittest
from glasgow_live.models import RSSEntry


class TestModels(unittest.TestCase):

    def setUp(self):
        self.time = datetime.datetime.now()

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

    def test_entry_data(self):
        entry = self.entry
        self.assertIs(entry.title, "test", "Expects a string")
        self.assertIs(entry.link, "test", "Expects a string")
        self.assertIs(entry.id, "test", "Expects a string")
        self.assertIs(entry.summary, "test", "Expects a string")
        self.assertIs(entry.published, "test", "Expects a string")
        self.assertIs(entry.author, "test", "Expects a string")
        self.assertIs(entry.media_keywords, "test test", "Expects a string")
        self.assertIs(entry.media_image, "test", "Expects a string")
