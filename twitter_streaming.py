# This file is part of TweetFetcher.

# TweetFetcher is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# TweetFetcher is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with TweetFetcher.  If not, see <http://www.gnu.org/licenses/>.

# Import the necessary package to process data in JSON format

from __future__ import print_function
from oslo_config import cfg
import json
import tools

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


class TwitterStreaming():

    def connect(self):
        # Initiate the connection to Twitter Streaming API
        return TwitterStream(auth=tools.setup())

    def get_data(self, twitter_stream):
        # Get a sample of the public data following through Twitter
        return twitter_stream.statuses.sample()

    def tweet_print(self, tweet):
        # print ("tweet from %s at %s saying :", tweet["user"]["id"], tweet["created_at"])
        try:
            print(tweet["text"])
        except KeyError:
            print("Tweet doesn't have a text field")

    def print_tweet(self):
        # Print each tweet in the stream to the screen
        # Here we set it to stop after getting 1000 tweets.
        # You don't have to set it to stop, but can continue running
        # the Twitter API to collect data for days or even longer.
        tweet_count = 1000
        for tweet in self.get_data(self.connect()):
            tweet_count -= 1

            # uncomment the line below to print all tweet's fields in Jason form
            # print(json.dumps(tweet, indent=4))

            # print only some fields of the tweet
            tools.tweet_minimal_print(tweet)

            if tweet_count <= 0:
                break
