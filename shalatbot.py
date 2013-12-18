#!/usr/bin/env python
# compatible with python 2.x and 3.x


import scheduler
import time
from datetime import datetime, timedelta
from prayertimes import PrayTimes
from pytz import timezone
import pytz
import datetime

#---------------------- prayTimes Object -----------------------
 
if __name__ == "__main__":
	from datetime import date
	
	print('Prayer Times for today in Mataram-NTB/Indonesia \n'+ ('='* 41))
	PT = PrayTimes('Egypt')
	times = PT.getTimes(date.today(),  [-8.58361,116.113683], +8)

	
	for i in ['Imsak','Subuh', 'Sunrise', 'Dhuhur', 'Ashar', 'Maghrib', 'Isha', 'Midnight']:
		time = datetime.datetime.utcnow() + datetime.timedelta(hours = +8)
		time = datetime.datetime(2013,7,10,19,21)
		
		#print i + ' : ' +times[i.lower()]
		#print i.lower() + ' :' + times[i.lower()]
		timeString = time.strftime("%H:%M")
		if (times[i.lower()] == timeString):
				if i.lower() == 'imsak' :
					print('Waktu ' + i+ ' Untuk Kota Mataram pukul' + ' '+ times[i.lower()] + ' WITA')
				elif i.lower() == 'sunrise' :
					print('Waktu Terbit Matahari Untuk Kota Mataram pukul' + ' '+ times[i.lower()] + ' WITA')
				elif i.lower() == 'maghrib' :
					print('Waktu Sholat ' + i+ ' Untuk Kota Mataram pukul' + ' '+ times[i.lower()] + ' WITA' + ' (Selamat Berbuka Puasa)')
				else :
					print('Waktu Sholat ' + i+ ' Untuk Kota Mataram pukul' + ' '+ times[i.lower()] + ' WITA')
						