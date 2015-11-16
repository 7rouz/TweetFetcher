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
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

def setup():
    # Config setup
    opt_group = cfg.OptGroup(name='twitter',
                                 title='Twitter API credentials')
    twitter_opts = [
        cfg.StrOpt('api_key', default=None,
                    help=('Twitter API Key')),
        cfg.StrOpt('api_secret', default=None,
                    help=('Twitter API Secret')),
        cfg.StrOpt('access_token', default=None,
                    help=('Twitter API Access Token')),
        cfg.StrOpt('access_token_secret', default=None,
                    help=('Twitter API Access Token secret'))
        ]
    CONF = cfg.CONF
    CONF.register_group(opt_group)
    CONF.register_opts(twitter_opts, opt_group)
    CONF(default_config_files=['app.conf'])

    # Variables that contains the user credentials to access Twitter API 
    ACCESS_TOKEN = CONF.twitter.access_token
    ACCESS_SECRET = CONF.twitter.access_token_secret
    CONSUMER_KEY = CONF.twitter.api_key
    CONSUMER_SECRET = CONF.twitter.api_secret

    return OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)