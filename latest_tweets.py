import requests

class LatestTweet:
    def __init__(self, username):
        self.username = username
        self.headers = { 'Authorization': r'Bearer TOKEN'}
        self.url = f"https://api.twitter.com/2/users/by/username/{self.username}?user.fields=profile_image_url"
    
    #def get_user_id(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.user_details = self.response.json()
        self.user_id = self.user_details['data']['id']
        self.name = self.user_details['data']['name']
        self.profile_image_url = self.user_details['data']['profile_image_url']
    
    #def get_latest_tweet(self):
        self.timeline_url = f"https://api.twitter.com/2/users/{self.user_id}/tweets?tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld&exclude=retweets,replies&max_results=5"
        self.response = requests.get(self.timeline_url, headers=self.headers)
        self.recent_tweets = self.response.json()
        self.tweet_text = self.recent_tweets['data'][0]['text']
        self.expanded_url = self.recent_tweets['data'][0]['entities']['urls'][0]['expanded_url']

