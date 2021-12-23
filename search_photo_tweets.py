import requests
import concurrent.futures


class TwitterAPI:
    def __init__(self, username):
        self.headers = {
            'Authorization': r'Bearer TOKEN'}

        self.profile_url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url"
        self.profile_response = requests.get(self.profile_url, headers=self.headers)
        self.profile_info = self.profile_response.json()

        self.id = self.profile_info['data']['id']
        self.name = self.profile_info['data']['name']
        self.url = f"https://api.twitter.com/2/users/{self.id}/tweets?tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,text,withheld&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld&exclude=retweets,replies&max_results=100"

        self.response = requests.get(self.url, headers=self.headers)
        self.picture_tweet_ids = []

        self.text = self.response.json()
        
        for i in range(100):
            try:
                if self.text['data'][i]['entities']['urls'][0]['expanded_url'].find("/photo") != -1:
                    self.picture_tweet_ids.append(self.text['data'][i]['id'])
            
            except KeyError:
                pass
            
