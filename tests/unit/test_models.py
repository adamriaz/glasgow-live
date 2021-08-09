import datetime
import unittest
from glasgow_live.models import RSSEntry, FacebookPost, TwitterTweet


class TestModels(unittest.TestCase):

    def setUp(self):
        self.time = datetime.datetime.now()

        self.entry = RSSEntry(
            title="test",
            link="test",
            id="test",
            summary="test",
            published="test",
            author="test",
            media_keywords="test test",
            media_image="test"
        )

        self.fb_post = FacebookPost(
            post_id="test",
            text="test",
            post_text="test",
            shared_text="test",
            time=self.time,
            image="test",
            image_lowquality="test",
            images=["test"],
            images_description=["test"],
            images_lowquality=["test"],
            images_lowquality_description=["test"],
            video="test",
            video_duration_seconds=10,
            video_height=800,
            video_id="test",
            video_quality="test",
            video_size_MB=100,
            video_thumbnail="test",
            video_watches=100,
            video_width=1280,
            likes=100,
            comments=100,
            shares=100,
            post_url="test",
            link="test",
            user_id="test",
            username="test",
            user_url="test",
            is_live=False,
        )

        self.twitter_tweet = TwitterTweet(
            id=1,
            id_str="test",
            conversation_id="test",
            datetime="test",
            datestamp="test",
            timestamp="test",
            user_id=1,
            user_id_str="test",
            username="test",
            name="test",
            place="test",
            timezone="test",
            mentions=["test"],
            reply_to=["test"],
            urls=["test"],
            video=100,
            thumbnail="test",
            tweet="test",
            lang="test",
            hashtags=["test"],
            cashtags=["test"],
            replies_count=1,
            retweets_count=1,
            likes_count=1,
            link="test",
            retweet=False,
            retweet_id="test",
            retweet_date="test",
            user_rt="test",
            user_rt_id="test",
            quote_url="test",
            near="test",
            geo="test",
            source="test",
            translate="test",
            trans_src="test",
            trans_dest="test",
        )

    def test_entry_data(self):
        entry = self.entry
        self.assertIs(entry.title, "test", "Expects a string")
        self.assertIs(entry.link, "test", "Expects a string")
        self.assertIs(entry.id, "test", "Expects a string")
        self.assertIs(entry.summary, "test", "Expects a string")
        self.assertIs(entry.published, "test", "Expects a string")
        self.assertIs(entry.author, "test", "Expects a string")
        self.assertIs(entry.media_keywords, "test test", "Expects a string")
        self.assertIs(entry.media_image, "test", "Expects a string")

    def test_facebook_post(self):
        post = self.fb_post
        self.assertIs(post.post_id, "test", "Expects a string")
        self.assertIs(post.text, "test", "Expects a string")
        self.assertIs(post.post_text, "test", "Expects a string")
        self.assertIs(post.shared_text, "test", "Expects a string")
        self.assertIs(post.time, self.time, "Expects a datetime")
        self.assertIs(post.image, "test", "Expects a string")
        self.assertIs(post.image_lowquality, "test", "Expects a string")
        self.assertListEqual(post.images, ["test"], "Expects a list[string]")
        self.assertListEqual(post.images_description, ["test"], "Expects a list[string]")
        self.assertListEqual(post.images_lowquality, ["test"], "Expects a list[string]")
        self.assertListEqual(post.images_lowquality_description, ["test"], "Expects a list[string]")
        self.assertIs(post.video, "test", "Expects a string")
        self.assertIs(post.video_duration_seconds, 10, "Expects an integer")
        self.assertIs(post.video_height, 800, "Expects an integer")
        self.assertIs(post.video_id, "test", "Expects a string")
        self.assertIs(post.video_quality, "test", "Expects a string")
        self.assertIs(post.video_size_MB, 100, "Expects an integer")
        self.assertIs(post.video_thumbnail, "test", "Expects a string")
        self.assertIs(post.video_watches, 100, "Expects an integer")
        self.assertIs(post.video_width, 1280, "Expects an integer")
        self.assertIs(post.likes, 100, "Expects an integer")
        self.assertIs(post.comments, 100, "Expects an integer")
        self.assertIs(post.shares, 100, "Expects an integer")
        self.assertIs(post.post_url, "test", "Expects a string")
        self.assertIs(post.link, "test", "Expects a string")
        self.assertIs(post.user_id, "test", "Expects a string")
        self.assertIs(post.username, "test", "Expects a string")
        self.assertIs(post.is_live, False, "Expects a boolean")

    def test_twitter_teet(self):
        tweet = self.twitter_tweet
        self.assertIs(tweet.id, 1, "Expects an integer")
        self.assertIs(tweet.id_str, "test", "Expects a string")
        self.assertIs(tweet.conversation_id, "test", "Expects a string")
        self.assertIs(tweet.datetime, "test", "Expects a string")
        self.assertIs(tweet.datestamp, "test", "Expects a string")
        self.assertIs(tweet.user_id, 1, "Expects an integer")
        self.assertIs(tweet.user_id_str, "test", "Expects a string")
        self.assertIs(tweet.username, "test", "Expects a string")
        self.assertIs(tweet.name, "test", "Expects a string")
        self.assertIs(tweet.place, "test", "Expects a string")
        self.assertIs(tweet.timezone, "test", "Expects a string")
        self.assertListEqual(tweet.mentions, ["test"], "Expects a list string")
        self.assertListEqual(tweet.reply_to, ["test"], "Expects a list string")
        self.assertListEqual(tweet.urls, ["test"], "Expects a list string")
        self.assertIs(tweet.video, 100, "Expects an integer")
        self.assertIs(tweet.thumbnail, "test", "Expects a string")
        self.assertIs(tweet.tweet, "test", "Expects a string")
        self.assertIs(tweet.lang, "test", "Expects a string")
        self.assertListEqual(tweet.hashtags, ["test"], "Expects a list string")
        self.assertListEqual(tweet.cashtags, ["test"], "Expects a list string")
        self.assertIs(tweet.replies_count, 1, "Expects an integer")
        self.assertIs(tweet.retweets_count, 1, "Expects an integer")
        self.assertIs(tweet.likes_count, 1, "Expects an integer")
        self.assertIs(tweet.link, "test", "Expects a string")
        self.assertIs(tweet.retweet, False, "Expects a boolean")
        self.assertIs(tweet.retweet_id, "test", "Expects a string")
        self.assertIs(tweet.quote_url, "test", "Expects a string")
        self.assertIs(tweet.near, "test", "Expects a string")
        self.assertIs(tweet.geo, "test", "Expects a string")
        self.assertIs(tweet.source, "test", "Expects a string")
        self.assertIs(tweet.translate, "test", "Expects a string")
        self.assertIs(tweet.trans_src, "test", "Expects a string")
        self.assertIs(tweet.trans_dest, "test", "Expects a string")
