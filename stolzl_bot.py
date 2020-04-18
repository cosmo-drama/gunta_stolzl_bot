import os
import random

import dotenv
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
import tweepy


# write a function that gets a random image file, and opens it
# basedir = '/Users/hadiya/PycharmProjects/textile_art_bot/stolzl'
# random_folder = random.choice(os.listdir(basedir))
# print(random_folder)
# title = random_folder
# sub_random_folder = random_folder
# print('"' + basedir + '/' + sub_random_folder + '"')
# new_dir = basedir + '/' + sub_random_folder
# random_file = random.choice(os.listdir(new_dir))
# print(random_file)
# random_file_directory = basedir + "/" + sub_random_folder + '/' + random_file
# print(random_file_directory)
# reader = Image.open(random_file_directory)
# reader.show()


# assemble tweet function where status=random_folder.title()

def twitter_api():
    api_key = os.getenv("API_KEY")
    api_secret_key = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api


twitter_api().home_timeline()
