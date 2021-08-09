# Glasgow Live
[![PyPI version](https://badge.fury.io/py/glasgow-live.svg)](https://pypi.org/project/glasgow-live)
[![codecov](https://codecov.io/gh/adamriaz/glasgow-live/branch/master/graph/badge.svg?token=0WQ27GBQ7C)](https://codecov.io/gh/adamriaz/glasgow-live)

A python module for news feeds from https://www.glasgowlive.co.uk/

## Installation

```bash
pip install glasgow-live
```
If you're having issues with Twint such as
```log
CRITICAL:root:twint.get:User:'NoneType' object is not subscriptable
```
Use:
```bash
pip install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

## Requires
- feedparser
- facebook-scraper
- twint

## Module Usage

```python
from glasgow_live import feed, rss_links

rss = feed.rss_feed(rss_links.GLASGOW_NEWS)

fb_posts = feed.facebook_feed(pages=3)

tweets = feed.twitter_feed(pages=1)
```