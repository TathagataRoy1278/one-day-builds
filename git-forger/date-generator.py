import datetime
import os
import random

d1 = input("Enter the Starting Date (yyyy/mm/dd) - ")
d2 = input("Enter the Ending date (yyyy/mm/dd) - ")

d1 = [int(i) for i in d1.split('/')]
d1 = datetime.datetime(d1[0], d1[1], d1[2], 0, 0, 0)

d2 = [int(i) for i in d2.split('/')]
d2 = datetime.datetime(d2[0], d2[1], d2[2], 0, 0, 0)

avg_commit_density = float('4.3')
tmp = input("Enter the average commit density per day, leave blank for default value of 4.3 : ")

if not tmp == '':
    avg_commit_density = float(tmp)

delta = d2 - d1
secs = delta.total_seconds()
os.system("echo > dates")
for i in range(int(delta.days * avg_commit_density)):
   os.system("echo %s >> dates"%str(d1+datetime.timedelta(seconds = random.randint(1, secs)))) 
