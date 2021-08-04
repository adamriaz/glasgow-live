_BASE_URL = "https://www.glasgowlive.co.uk"
_RSS_SERVICE = "?service=rss"

# NEWS MENU
_NEWS = "news"
_ALL_ABOUT = "all-about"

LATEST_NEWS = f"{_BASE_URL}/{_NEWS}/{_RSS_SERVICE}"
GLASGOW_NEWS = f"{_BASE_URL}/{_NEWS}/glasgow-news/{_RSS_SERVICE}"
CRIME = f"{_BASE_URL}/{_ALL_ABOUT}/crime{_RSS_SERVICE}"
HEALTH = f"{_BASE_URL}/{_NEWS}/health/{_RSS_SERVICE}"
EDUCATION = f"{_BASE_URL}/{_ALL_ABOUT}/education/{_RSS_SERVICE}"
POLITICS = f"{_BASE_URL}/{_ALL_ABOUT}/politics/{_RSS_SERVICE}"
TRAVEL = f"{_BASE_URL}/{_ALL_ABOUT}/traffic-and-travel/{_RSS_SERVICE}"
BUSINESS = f"{_BASE_URL}/business/{_RSS_SERVICE}"
HISTORY = f"{_BASE_URL}/{_NEWS}/history/{_RSS_SERVICE}"
WORLD_NEWS = f"{_BASE_URL}/{_NEWS}/world-news/{_RSS_SERVICE}"
NEWS_OPINION = f"{_BASE_URL}/{_NEWS}/news-opinion/{_RSS_SERVICE}"

# SPORT MENU
_SPORT = "sport"
SPORT_NEWS = f"{_BASE_URL}/{_SPORT}/{_RSS_SERVICE}"
CELTIC_FC = f"{_BASE_URL}/{_ALL_ABOUT}/celtic-fc/{_RSS_SERVICE}"
RANGERS_FC = f"{_BASE_URL}/{_ALL_ABOUT}/rangers-fc/{_RSS_SERVICE}"
OTHER_SPORT = f"{_BASE_URL}/{_SPORT}/other-sport/{_RSS_SERVICE}"
