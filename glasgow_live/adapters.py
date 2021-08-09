import feedparser
import facebook_scraper
import twint
from typing import Any, Iterator
from models import RSSEntry, FacebookPost, TwitterTweet


class TwitterFeedAdapter:

    def __init__(self, page_name: str):
        self._twint = twint
        self._twitter = self._twint.Config()
        self._twitter.Hide_output = True
        self._twitter.Username = page_name

    def _get_tweets(self, pages: int = 1) -> list:
        try:
            posts = []
            self._twitter.Limit = pages
            self._twitter.Store_json = True
            self._twitter.Store_object = True
            self._twitter.Store_object_tweets_list = posts
            self._twint.run.Search(self._twitter)
            return posts
        except Exception as e:
            raise ValueError(f"Error occurred on Twitter Feed. {e}")

    def get_data(self, pages: int = 1) -> list:
        """
        Returns tweets from Twitter page.

        :param pages: Limit number of twitter pages
        :return: TwitterTweet results
        """
        tweets = []
        tweets_fetched = self._get_tweets(pages)
        for item in tweets_fetched:
            tweet = TwitterTweet(
                id=item.id if hasattr(item, 'id') else None,
                id_str=item.id_str if hasattr(item, 'id_str') else None,
                conversation_id=item.conversation_id if hasattr(item, 'conversation_id') else None,
                datetime=item.datetime if hasattr(item, 'datetime') else None,
                datestamp=item.datestamp if hasattr(item, 'datestamp') else None,
                timestamp=item.timestamp if hasattr(item, 'timestamp') else None,
                user_id=item.user_id if hasattr(item, 'user_id') else None,
                user_id_str=item.user_id_str if hasattr(item, 'user_id_str') else None,
                username=item.username if hasattr(item, 'username') else None,
                name=item.name if hasattr(item, 'name') else None,
                place=item.place if hasattr(item, 'place') else None,
                timezone=item.timezone if hasattr(item, 'timezone') else None,
                mentions=item.mentions if hasattr(item, 'mentions') else None,
                reply_to=item.reply_to if hasattr(item, 'reply_to') else None,
                urls=item.urls if hasattr(item, 'urls') else None,
                video=item.video if hasattr(item, 'video') else None,
                thumbnail=item.thumbnail if hasattr(item, 'thumbnail') else None,
                tweet=item.tweet if hasattr(item, 'tweet') else None,
                lang=item.lang if hasattr(item, 'lang') else None,
                hashtags=item.hashtags if hasattr(item, 'hashtags') else None,
                cashtags=item.cashtags if hasattr(item, 'cashtags') else None,
                replies_count=item.replies_count if hasattr(item, 'replies_count') else None,
                retweets_count=item.retweets_count if hasattr(item, 'retweets_count') else None,
                likes_count=item.likes_count if hasattr(item, 'likes_count') else None,
                link=item.link if hasattr(item, 'link') else None,
                retweet=item.retweet if hasattr(item, 'retweet') else None,
                retweet_id=item.retweet_id if hasattr(item, 'retweet_id') else None,
                retweet_date=item.retweet_date if hasattr(item, 'retweet_date') else None,
                user_rt=item.user_rt if hasattr(item, 'user_rt') else None,
                user_rt_id=item.user_rt_id if hasattr(item, 'user_rt_id') else None,
                quote_url=item.quote_url if hasattr(item, 'quote_url') else None,
                near=item.near if hasattr(item, 'near') else None,
                geo=item.geo if hasattr(item, 'geo') else None,
                source=item.source if hasattr(item, 'source') else None,
                translate=item.translate if hasattr(item, 'translate') else None,
                trans_src=item.trans_src if hasattr(item, 'trans_src') else None,
                trans_dest=item.trans_dest if hasattr(item, 'trans_dest') else None,
            )
            tweets.append(tweet.__dict__)

        return tweets


class FacebookFeedAdapter:

    def __init__(self, page_name: str):
        self._facebook_scraper = facebook_scraper
        self._page_name = page_name

    def _get_posts(self, pages: int = 3) -> Iterator:
        try:
            return self._facebook_scraper.get_posts(account=self._page_name, pages=pages)
        except Exception as e:
            raise ValueError(f"Error occurred on Facebook Feed. {e}")

    def get_data(self, pages: int = 3) -> list:
        """
        Returns posts from Facebook page.

        :param pages: Limit number of facebook pages
        :return: FacebookPost results
        """
        posts = []
        for item in self._get_posts(pages):
            post = FacebookPost(
                post_id=item['post_id'] if 'post_id' in item else None,
                text=item['text'] if 'text' in item else None,
                post_text=item['post_text'] if 'post_text' in item else None,
                shared_text=item['shared_text'] if 'shared_text' in item else None,
                time=item['time'] if 'time' in item else None,
                image=item['image'] if 'image' in item else None,
                image_lowquality=item['image_lowquality'] if 'image_lowquality' in item else None,
                images=item['images'] if 'images' in item else None,
                images_description=item['images_description'] if 'images_description' in item else None,
                images_lowquality=item['images_lowquality'] if 'images_lowquality' in item else None,
                images_lowquality_description=item['images_lowquality_description'] if 'images_lowquality_description' in item else None,
                video=item['video'] if 'video' in item else None,
                video_duration_seconds=item['video_duration_seconds'] if 'video_duration_seconds' in item else None,
                video_height=item['video_height'] if 'video_height' in item else None,
                video_id=item['video_id'] if 'video_id' in item else None,
                video_quality=item['video_quality'] if 'video_quality' in item else None,
                video_size_MB=item['video_size_MB'] if 'video_size_MB' in item else None,
                video_thumbnail=item['video_thumbnail'] if 'video_thumbnail' in item else None,
                video_watches=item['video_watches'] if 'video_watches' in item else None,
                video_width=item['video_width'] if 'video_width' in item else None,
                likes=item['likes'] if 'likes' in item else None,
                comments=item['comments'] if 'comments' in item else None,
                shares=item['shares'] if 'shares' in item else None,
                post_url=item['post_url'] if 'post_url' in item else None,
                link=item['link'] if 'link' in item else None,
                user_id=item['user_id'] if 'user_id' in item else None,
                username=item['username'] if 'username' in item else None,
                user_url=item['user_url'] if 'user_url' in item else None,
                is_live=item['is_live'] if 'is_live' in item else None,
            )
            posts.append(post.__dict__)
        return posts


class RSSFeedAdapter:

    def __init__(self, url: str):
        self._feedparser = feedparser
        self._url = url

    def _get_entries(self) -> any:
        try:
            return self._feedparser.parse(self._url)["entries"]
        except Exception as e:
            raise ValueError(f"Error occurred on RSS Feed. {e}")

    def get_rss_data(self) -> list:
        """
        Returns the results from RSS url.

        :param url: RSS url
        :return: RSSEntry results
        """
        entries = self._get_entries()
        entries_data = []
        for item in entries:
            entry = RSSEntry(
                title=item["title"] if "title" in item else None,
                link=item["link"] if "link" in item else None,
                id=item["id"] if "id" in item else None,
                summary=item["summary"] if "summary" in item else None,
                published=item["published"] if "published" in item else None,
                author=item["author"] if "author" in item else None,
                media_keywords=item["media_keywords"] if "media_keywords" in item else None,
                media_image=item["media_content"][0]["url"] if "media_content" in item
                                                               and len(item["media_content"]) > 0 else None
            )
            entries_data.append(entry.__dict__)

        return entries_data
