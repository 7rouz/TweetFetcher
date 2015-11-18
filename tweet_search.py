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

import tools
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import tweepy
import datetime


class TweetSearch():

    def connect(self):
        # Initiate the connection to Twitter REST API
        return Twitter(auth=tools.setup())

    def hashtag_search(self, hashtag):
        # Search for latest tweets about hastag
        api = tools.tweepy_setup()
        i = datetime.datetime.now()

        for tweet in tweepy.Cursor(api.search, q=hashtag, count=1, lang="en", since_id=int(i.year) - int(i.month) - int(i.day)).items():
            print tweet.created_at, tweet.text

    def location_check(self, location_name):
        # Get all the locations where Twitter provides trends service
        # The places ids are WOEIDs (Where On Earth ID), which are 32-bit identifiers provided by Yahoo! GeoPlanet project.
        # And yes! Twitter is very international.
        world_trends = self.connect().trends.available(_woeid=1)
        for location in world_trends:
            if self.get_woeid(location, location_name) is not None:
                return self.get_woeid(location, location_name)

    def get_locations_list(self):
        world_trends = self.connect().trends.available(_woeid=1)
        locations = []
        for location in world_trends:
            locations.append(location["name"])
        return locations

    def get_woeid(self, location, location_name):
        # print("this location is %s and the needed location is %s ",
        #       location["name"],
        #       location_name)
        if location["name"] == location_name:
            return location["woeid"]
        else:
            return None

    def get_trends(self, location):
        trends_list = []
        if self.location_check(location) is None:
            print("Sorry, the chosen location doesn't support trend search !!")
        else:
            trends = self.connect().trends.place(_id=self.location_check(location))
            for trend in trends[0]["trends"]:
                trends_list.append(trend["name"])
        return trends_list

    def get_trends_one_location(self):
        location = tools.location_cfg()["location"]
        return self.get_trends(location)

    def get_trends_all_locations(self):
        trends_list = []
        locations = tools.location_setup()["locations list"]
        for location in locations:
            trends_list.append(
                {'location': location,
                 'trends': self.get_trends(location)})
        return trends_list
