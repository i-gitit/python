#!/usr/bin/python3
import datetime
name=input("enter you name : ")
age=int(input("enter your age"))

now=datetime.datetime.now()
curr=now.year
year=curr+(95-age)
print("Mr/Ms "+name+" your age will be 95 in year ",year)
