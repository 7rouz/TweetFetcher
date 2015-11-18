<snippet>
  <content>
# TweetFetcher

I started this project with the purpose of having one project that contains all the possible functionalities that one could need when using Twitter.
For the moment I have used Two APIs which are :
- twitter
- Tweepy
and here is the list of implemented functionalities :
- live steaming 
- getting trends (worldwide and by region)
- fetching tweets by hashtags or key words

## Installation

To start with, you will need to have a Twitter account and obtain credentials (i.e. API key, API secret, Access token and Access token secret) on the Twitter developer site to access the Twitter API, following these steps:

- Create a Twitter user account if you do not already have one.
- Go to [link to twitter API](https://apps.twitter.com) and log in with your Twitter user account. This step gives you a Twitter dev account under the same name as your user account.
- Click "Create New App"
- Fill out the form, agree to the terms, and click "Create your Twitter application"
- In the next page, click on "Keys and Access Tokens" tab, and copy your "API key" and "API secret". Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".
Once you have your credentials you should go to app.conf file and put them there (without the ""):
api_key = API key
api_secret = API secret
access_token = Access token
access_token_secret = Access token secret
Now save the file and go to your favorite Terminal and go under the TweetFetcher directory:
- First launch this command ` pip install requirements `

## Usage

if installation ended normally you can run the project by using the following command line 
```python app.py```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

I would like to thank [WEI XU] (http://www.cis.upenn.edu/~xwe/) for this helpful [Tutorial] (http://socialmedia-class.org/twittertutorial.html)

## License

TweetFetcher is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

TweetFetcher is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with TweetFetcher.  If not, see <http://www.gnu.org/licenses/>.


**THE** **END**
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
</content>
  <tabTrigger>readme</tabTrigger>
</snippet>
