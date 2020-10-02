
import tweepy
import os
import time

def create_api():
  consumer_key = os.getenv('consumer_key')
  consumer_secret = os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  # api = tweepy.API(auth)

  api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
def follower_count(user):
  emoji_num = {0:'0️⃣', 1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣'}
  uf_split = [int(i) for i in str(user.followers_count)]
  fol_split_emoji = ''.join([emoji_num[j] for j in uf_split if j in emoji_num.keys()])
  return fol_split_emoji

api = create_api()

while True:
  user = api.get_user('laasyasrivanka')
  api.update_profile(name = f'LAASYA {follower_count(user)} ')
  print(f'Updating Twitter Name : LAASYA {follower_count(user)} ')
  print('Waiting to Refresh')
  time.sleep(60)
  
