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


# Main function here
if __name__ == "__main__":
    # ts = TwitterStreaming()
    # ts.print_tweet()
    tweet = TweetSearch()
    # tweet.hashtag_search("#PrayForParis")
    tweet.get_trends(1)