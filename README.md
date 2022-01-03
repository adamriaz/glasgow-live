# Glasgow Live
[![PyPI version](https://badge.fury.io/py/glasgow-live.svg)](https://pypi.org/project/glasgow-live)
[![codecov](https://codecov.io/gh/adamriaz/glasgow-live/branch/master/graph/badge.svg?token=0WQ27GBQ7C)](https://codecov.io/gh/adamriaz/glasgow-live)

A python module for news feeds from https://www.glasgowlive.co.uk/

## Installation

```bash
pip install glasgow-live
```

## Requires
- feedparser

## Module Usage

```python
from glasgow_live import feed, rss_links

rss = feed.rss_feed(rss_links.GLASGOW_NEWS)
```