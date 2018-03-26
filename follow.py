import tweepy

USER_NUMBER=2
HASHTAG='iot'
FILENAME='users.txt'
MIN_NUMBER_OF_FRIENDS=100

consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Count number of friends
def get_friends(follower):
    return follower.author.friends_count

    # users = []
    # page_count = 0
    # for i, user in enumerate(tweepy.Cursor(api.friends, screen_name=user_id).pages()):
    #     users += user
    # print("User "+ user_id + " has " + len(users) + " friends")
    # return len(users)



if __name__ == "__main__":

    # Create the file to store user names
    file = open(FILENAME,'w')

    remaining_users=USER_NUMBER

    # Find users tweeting about a specific hashtag
    for follower in tweepy.Cursor(api.search, q=HASHTAG).items(1000):
        friends_number=get_friends(follower)
        if friends_number>MIN_NUMBER_OF_FRIENDS:
            print("User followed: " + follower.author.screen_name + ", " + str(friends_number)+ " friends")
            file.write(follower.author.screen_name+'\n')
            user = api.get_user(screen_name = follower.author.screen_name)
            user.follow()
            remaining_users-=1
            if remaining_users==0:
                break
        else:
            print("User " + " only has " + str(friends_number) + " friends. Dont follow")
