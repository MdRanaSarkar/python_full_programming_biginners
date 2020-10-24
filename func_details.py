"""
import time
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

import  calendar

cal=calendar.month(2020,3)
print(cal)

import time
t=(2020,10,4,14,4,40,1,48,0)
d=time.mktime(t)

print(d)
localti=time.asctime(time.localtime(d))
localt=time.strftime('%b %d %Y %H:%M:%S',time.localtime(d))
print("%s" %localti)
print("%s" %localt)



import re
line="Cats are the smaller"
matcho=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matcho:
    print(matcho.group(1))
else:
    print('no match')


import re
line="Cats are the Smaller"

matching=re.search(r'smaller',line,re.M|re.I)
if matching:
    print(matching.group())
else:
    print('No matching ')

"""

def humandetail(age,country='india'):
    "here print age and country of human"
    print('Age :',age)
    print('Country :' ,country)
humandetail(37,'bd')
humandetail(37)