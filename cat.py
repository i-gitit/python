#!/usr/bin/python3
#INPUT IN FORMAT 'python3 cat.py [files locations]'
import sys
import os
x=sys.argv[1:]
for i in x:
	try:
		f=open(i,'r')
		print(f.read())
		f.close()
	except:
		print("File: '"+i+"' not displayed")
