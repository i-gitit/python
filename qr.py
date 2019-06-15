#!/usr/bin/python
from googlesearch import search
import pyqrcode
import os
a=0
s=input("enter your search")
l=search(s,tld='com',lang='en',num=3,start=0,stop=3,pause=1) 
for i in l:
    q=pyqrcode.create(i)
    print(i)
    q.png("qr{}.png".format(a),scale=5)
    os.system(" scp -i < location of key > qr"+str(a)+".png ec2-user@< ip of aws instance >:/var/www/html/") #relpace <> with req details
    a=a+1

#in aws machine grant write permissions  to other category for /var/www/html
