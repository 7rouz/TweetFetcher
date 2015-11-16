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


class TweetSearch():
	def connect(self):
		# Initiate the connection to Twitter REST API
		return Twitter(auth= tools.setup())

	def hashtag_search(self, hashtag):
		# Search for latest tweets about "#nlproc"
		self.connect().search.tweets(q=hashtag)

	def get_trends(self, woeid):
		# Get all the locations where Twitter provides trends service
		# The places ids are WOEIDs (Where On Earth ID), which are 32-bit identifiers provided by Yahoo! GeoPlanet project.
		# And yes! Twitter is very international.
		world_trends = self.connect().trends.available(_woeid= woeid)
		print (json.dumps(world_trends, indent=4))