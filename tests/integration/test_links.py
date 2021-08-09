import unittest

import requests

import glasgow_live.rss_links as rss_links


class TestLinks(unittest.TestCase):

    def get_all_links(self):
        links = [
            rss_links.LATEST_NEWS, rss_links.GLASGOW_NEWS, rss_links.CRIME, rss_links.HEALTH, rss_links.EDUCATION,
            rss_links.POLITICS, rss_links.TRAVEL, rss_links.BUSINESS, rss_links.HISTORY, rss_links.WORLD_NEWS,
            rss_links.NEWS_OPINION, rss_links.SPORT_NEWS, rss_links.CELTIC_FC, rss_links.RANGERS_FC,
            rss_links.OTHER_SPORT, rss_links.SPECIAL_FEATURES, rss_links.PROPERTY, rss_links.LIFE_STYLE,
            rss_links.GLASGOW_LIVES]
        return links

    def test_all_links(self):
        for link in self.get_all_links():
            response = requests.get(link)
            self.assertTrue(response.ok, msg=f"expects response to be 200(OK). {response} from {link}")
