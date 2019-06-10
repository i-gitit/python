#!/usr/bin/python3

import datetime
now=datetime.datetime.now()

hour=now.hour
if hour>=20 :
	print("good night")
elif hour>=17 :
	print("good evening")
elif hour>=12 :
	print("good afternoon")
elif hour>=6 :
	print("good morning")
else:
	print("good night")

