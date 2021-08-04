import unittest

import requests

from glasgow_live.rss_links import LATEST_NEWS, GLASGOW_NEWS, CRIME, HEALTH, EDUCATION, POLITICS, TRAVEL, \
    BUSINESS, HISTORY, WORLD_NEWS, NEWS_OPINION, SPORT_NEWS, CELTIC_FC, RANGERS_FC, OTHER_SPORT


class TestLinks(unittest.TestCase):

    def get_all_links(self):
        links = [LATEST_NEWS, GLASGOW_NEWS, CRIME, HEALTH, EDUCATION, POLITICS, TRAVEL,
                 BUSINESS, HISTORY, WORLD_NEWS, NEWS_OPINION, SPORT_NEWS, CELTIC_FC, RANGERS_FC, OTHER_SPORT]
        return links

    def test_all_links(self):
        for link in self.get_all_links():
            response = requests.get(link)
            self.assertTrue(response.ok, msg=f"expects response to be 200(OK). {response} from {link}")
