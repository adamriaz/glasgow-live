from adapter import FeedAdapter
from links import NEWS
from models import Entry


def get_feed():
    return FeedAdapter().get_data(NEWS)


if __name__ == "__main__":
    data: list[Entry] = get_feed()
    for item in data:
        print(item.to_json())
