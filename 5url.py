#!/urs/bin/python3
from googlesearch import search
data=input("enter what to search : ")
x=search(data, stop=5)
#os.chdir("/home/adhoc/Desktop/")
file=open("urls.txt",'w')
for i in x :
	print(i)
	file.write(i+'\n')

