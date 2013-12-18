#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db
from django.utils import simplejson as json
import tweepy
import sys
import os
import urllib
import pprint
from optparse import OptionParser
from xml.dom.minidom import parse
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import datetime
import urllib2
import time
from prayertimes import PrayTimes


class TweetLog(db.Model):
    username = db.StringProperty()
    replied_on = db.DateTimeProperty(auto_now=True)

    @staticmethod
    def get(tweet_id):
        tweet_id = str(tweet_id)
        tweetlog = TweetLog.get_by_key_name(tweet_id)
        return tweetlog

    @staticmethod
    def set(tweet_id, username):
        Config(key_name=str(tweet_id),
               username=username
               ).put()

class MataramPrayerTimes(webapp.RequestHandler):

	def get(self):
		consumer_key = "F6IDVs26q1D93u7ChCcGQ"
		consumer_secret = "V1ucn0kbaMNMPORWnhVETlZJGL5bHOdTewUW5VTR4"
		access_token = "410814371-87pWoeU3KhSaH4ATk1QJfZ6zvGpUj8YlXU7Mh5Ga"
		access_token_secret = "QQoGEKVZRXLRtrd7agRNmJUB6YqvEf5GXCxWNenpsI"
		
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)
		prayTimes = PrayTimes()
		
		from datetime import date
		PT = PrayTimes('Egypt')
		times = PT.getTimes(date.today(), (-8.58,116.11), +8);
	
		for i in ['Imsak','Subuh', 'Sunrise', 'Dhuhur', 'Ashar', 'Maghrib', 'Isha']:
			time = datetime.datetime.utcnow() + datetime.timedelta(hours = 8)
			timeString = time.strftime("%H:%M")
			
			if (times[i.lower()] == timeString):
				if i.lower() == 'imsak' :
					self.response.out.write('Waktu ' + i+ ' Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
					api.update_status('Waktu ' + i+ ' Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
				elif i.lower() == 'sunrise' :
					self.response.out.write('Waktu Terbit Matahari Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
					api.update_status('Waktu Terbit Matahari Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
				elif i.lower() == 'maghrib' :
					self.response.out.write('Waktu Sholat ' + i+ ' Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
					api.update_status('Waktu Sholat ' + i+ ' Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
				else :
					self.response.out.write('Waktu Sholat ' + i+ ' Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
					api.update_status('Waktu Sholat ' + i+ ' Untuk Kota Mataram pada pukul' + ' '+ times[i.lower()] + ' WITA')
		
class Test(webapp.RequestHandler):
	def get(self):
		self.response.out.write('Hello World')
		
def main():
    application = webapp.WSGIApplication([
            ('/', MataramPrayerTimes)],
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
	



