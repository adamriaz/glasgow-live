import unittest

import requests

from glasgow_live.links import NEWS


class TestLinks(unittest.TestCase):

    def test_news(self):
        news_response = requests.get(NEWS)
        self.assertTrue(news_response.ok, msg=f"expects response to be 200(OK). {news_response}")
