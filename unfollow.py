import tweepy

FILENAME='users.txt'

consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
my_user_name=api.me().screen_name


with open(FILENAME) as f:
    userlist = f.readlines()
    userlist = [x.strip() for x in userlist]

for user in userlist:
    try:
        status = api.show_friendship(source_screen_name =my_user_name,target_screen_name =user)
        if (status[0].following and status[1].following):
            print(user + " has followed us back. Don't do anything")
        else:
            print(user + " hasn't followed us back. Unfollow.")
            t_user=api.get_user(screen_name=user)
            t_user.unfollow()
    except:
        print(user + " doesn't seem to exist")
