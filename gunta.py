import os
import random
import tweepy
from PIL import Image
from dotenv import load_dotenv


load_dotenv()


def twitter_api():
    api_key = os.getenv("API_KEY")
    api_secret_key = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api


# write a function that gets a random image file, and opens it
def select_random_image():
    basedir = '/Users/hadiya/PycharmProjects/textile_art_bot/stolzl'
    random_folder = random.choice(os.listdir(basedir))
    print(random_folder)
    title = random_folder
    sub_random_folder = random_folder
    # print('"' + basedir + '/' + sub_random_folder + '"')
    new_dir = basedir + '/' + sub_random_folder
    print(new_dir)
    random_image = random.choice(os.listdir(new_dir))
    print(random_image)
    random_image_directory = basedir + "/" + sub_random_folder + '/' + random_image
    print(random_image_directory)
    # reader = Image.open(random_image_directory)
    # reader.show()
    return {'title': title, 'random_image': random_image, 'random_image_directory': random_image_directory}


def assemble_tweet(selection):
    title = selection['title']
    random_image = selection['random_image']
    im_dir = selection['random_image_directory']
    tweet = "'" + title + "'\n" + "#bauhaus #guntastolzl #textilearts"
    twitter_api().update_with_media(filename=im_dir, status=tweet)
    print("tweet sent.")


selections = select_random_image()
assemble_tweet(selections)
