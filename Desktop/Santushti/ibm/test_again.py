import time
import tweepy
import csv

consumer_key = 'eeSnutOqqknGGGqiso8DPEfdn'
consumer_secret = 'uqKKBzpp96NJTBwEBge9wmsVKEJBdoSuMOmsaQiUphikReuJaH'
access_token = "1276097905363828736-RQfCc3FuSvhdwyYhjpoDfO7QH6Q4gB"
access_token_secret = "nL8jdSU1j0cuRNiGGum8uTaLrq0blGEwqI8kmfwzAMSsJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#results = api.search('#covid', count=100, lang="en", since="2020-01-01")

csvFile = open('hackathon.csv','w')
csvwriter = csv.writer(csvFile)

for item in tweepy.Cursor(api.search,q="#covid",count=100,
                           lang="en",
                           since="2020-01-01").items():
	csvwriter.writerow([item.user.screen_name.encode("utf-8"),item.text.encode("utf-8"),item.user.followers_count])
