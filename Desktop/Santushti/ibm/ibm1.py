import tweepy
import csv
import pandas as pd
####input your credentials here

consumer_key = 'eeSnutOqqknGGGqiso8DPEfdn'
consumer_secret = 'uqKKBzpp96NJTBwEBge9wmsVKEJBdoSuMOmsaQiUphikReuJaH'
access_token = '1276097905363828736-RQfCc3FuSvhdwyYhjpoDfO7QH6Q4gB'
access_token_secret = 'nL8jdSU1j0cuRNiGGum8uTaLrq0blGEwqI8kmfwzAMSsJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('hackathon.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)

csvWriter.writerow(["Screen_Name", "Tweet_Text", "Follower_Count"])

for tweet in tweepy.Cursor(api.search,q="#covid",lang="en",
                           since="2020-01-01").items():
    print (tweet.created_at, tweet.text)
    #csvWriter.writerow([tweet.text.encode('utf-8')])
    csvWriter.writerow([tweet.user.screen_name.encode("utf-8"),tweet.text.encode("utf-8"), tweet.user.followers_count])
