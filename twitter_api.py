import requests
import random
from search_photo_tweets import TwitterAPI

class Posts:
    def __init__(self, username):
        tapi = TwitterAPI(username)
        
        self.list = tapi.picture_tweet_ids
        self.url = f"https://api.twitter.com/2/tweets/{random.choice(self.list)}?tweet.fields=text&expansions=attachments.media_keys&media.fields=url"

        self.headers = { 'Authorization': r'Bearer {BEARER TOKEN}'}

        self.response = requests.get(self.url, headers=self.headers)

        self.x = self.response.json()
        self.text = self.x["data"]["text"]
        self.image_url = self.x["includes"]["media"][0]["url"]
        self.name = tapi.name