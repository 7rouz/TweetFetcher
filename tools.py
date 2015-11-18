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
import tweepy
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


def tweepy_setup():
    credentials = credential_cfg()
    auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'],
                               credentials['CONSUMER_SECRET'])
    auth.set_access_token(credentials['ACCESS_TOKEN'],
                          credentials['ACCESS_SECRET'])
    api = tweepy.API(auth)
    return api


def setup():
    credentials = credential_cfg()
    return OAuth(credentials['ACCESS_TOKEN'],
                 credentials['ACCESS_SECRET'],
                 credentials['CONSUMER_KEY'],
                 credentials['CONSUMER_SECRET'])


def credential_cfg():
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

    return {'ACCESS_TOKEN': CONF.twitter.access_token,
            'ACCESS_SECRET': CONF.twitter.access_token_secret,
            'CONSUMER_KEY': CONF.twitter.api_key,
            'CONSUMER_SECRET': CONF.twitter.api_secret}


def location_cfg():
    # Config setup
    opt_group = cfg.OptGroup(name='key_words',
                             title='location and locations list')
    location_opts = [
        cfg.StrOpt('location', default='Worldwide',
                   help=('location for tweet search')),
        cfg.ListOpt('locations_list', default=[],
                    help=('list of all the locations available'))
    ]
    CONF = cfg.CONF
    CONF.register_group(opt_group)
    CONF.register_opts(location_opts, opt_group)
    CONF(default_config_files=['app.conf'])

    # Variables that contains the user credentials to access Twitter API
    LOCATION = CONF.key_words.location
    LOCATIONS_LIST = CONF.key_words.locations_list

    return {'location': LOCATION, 'locations list': LOCATIONS_LIST}


def tweet_minimal_print(tweet):
    try:
        if 'text' in tweet:  # only messages contains 'text' field is a tweet
            print(tweet['id'])  # This is the tweet's id
            print(tweet['created_at'])  # when the tweet posted
            print(tweet['text'])  # content of the tweet

            print(tweet['user']['id'])  # id of the user who posted the tweet
            print(tweet['user']['name'])  # name of the user, e.g. "Wei Xu"
            # name of the user account, e.g. "cocoweixu"
            print(tweet['user']['screen_name'])

            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
            print(hashtags)
            print("\n")

    except:
        # read in a line is not in JSON format (sometimes error occured)
        pass
