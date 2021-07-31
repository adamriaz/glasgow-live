from adapter import FeedAdapter
from entry_data import Entry


def get_feed():
    return FeedAdapter().get_data("https://www.glasgowlive.co.uk/news/?service=rss")


if __name__ == "__main__":
    data: list[Entry] = get_feed()
    for item in data:
        print(item.to_json())
