# twitterbot
Twitter bot that automatically:
- Follows users that has tweeted with an specific hashtag
- Unfollows users that are not following you back

## Getting prepared
In order to use this bot you will need the following packages installed in your computer:
- Python 3 (https://www.python.org/downloads/)
- Tweepy 3.6.0 library (http://docs.tweepy.org/en/v3.6.0/install.html) 

## Configuration parameters
The bot has certain configuration parameters that needs to be setup before running. You can change these parameters in the 'follow.py', 'unfollow.py' files:
USER_NUMBER: Number of users that the the bot will follow when executing follow.py
HASHTAG=specific hashtag the bot will search to follow users when executing follow.py
FILENAME=name of the file where the accounts followed or unfollowed will be stored
MIN_NUMBER_OF_FRIENDS=Minimum number of friends that the bot will consider to make an account followable

consumer_key=String with the twitter consumer key (see twitter documentation for this)
consumer_secret=String with the twitter consumer secret (see twitter documentation for this)
access_token=String with the access token (see twitter documentation for this)
access_token_secret=String with the access token secret (see twitter documentation fo this)

#How to
1. Clone the repo
2. Set up your configuration parameters by editing follow.py and unfollow.py
3. Execute python3 follow.py, this will result in a file with the accounts followed
4. Wait some days and execute python3 unfollow.py, this will unfollow those accounts in the file which didn't followed us back
