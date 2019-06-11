#!/usr/bin/python3
#GIVE INPUT IN FORMAT python3 touch.py [files name]  eg: python3 touch.py hello.txt
import sys
x=sys.argv[1:]
for i in x :
	try:
		f=open(i,'r+')
	except:
		print("file doesn't exist creating new file")
		f=open(i,'w')	
