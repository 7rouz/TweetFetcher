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

from __future__ import print_function
from oslo_config import cfg
from twitter_streaming import TwitterStreaming
from tweet_search import TweetSearch
import json
import tools


# Main function here
if __name__ == "__main__":
    # Live tweet this code block gets tweets from your twitter page
    # Twitter streaming
    ts = TwitterStreaming()
    # ts.print_tweet()
    # this block searches among all tweets by hashtag or key words or users
    tweet = TweetSearch()
    print(json.dumps(tweet.get_trends_one_location(), indent=4))
    # this one is too much for the API to handle
    # I am afread that this one can't be done beacause of Rate limits in version 1.1 of the API
    # print(json.dumps(tweet.get_trends_all_locations(), indent=4))
    print(tweet.hashtag_search('#PSYSomewhereDownTheRoad'))
