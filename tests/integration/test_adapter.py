import unittest

from glasgow_live.models import Entry


class TestAdapter(unittest.TestCase):

    def setUp(self):
        self.entry = Entry(
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
