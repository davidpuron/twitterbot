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
my_user_name=api.me().screen_name

# Count number of friends
def get_friends(follower):
    return follower.author.friends_count

# check if we are already following the target user (in order to not repeat)
def is_friend(target_user):
    status = api.show_friendship(source_screen_name = target_user,target_screen_name =my_user_name)
    if (status[1].following):
        return True
    else:
        return False


if __name__ == "__main__":

    HASHTAG=raw_input("Introduce el hashtag a seguir: ")
    USER_NUMBER=int(raw_input("Introduce el numero de usuarios a seguir: "))
    MIN_NUMBER_OF_FRIENDS=int(raw_input("Introduce el minimo numero de seguidores que tiene que tener un usuario para ser seguido: "))
    

    # Create the file to store user names
    file = open(FILENAME,'w')

    remaining_users=USER_NUMBER

    # Find users tweeting about a specific hashtag
    for follower in tweepy.Cursor(api.search, q=HASHTAG).items(1000):
        if (is_friend(follower.author.screen_name)):
            print(follower.author.screen_name + " is already followed, don't do anything")
        else:
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
