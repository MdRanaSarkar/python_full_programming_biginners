import time

tick=time.time()
print("present time",tick)

print("local time : ",time.localtime())

print("fixed local time : ",time.asctime( time.localtime(time.time()) ))

t=time.localtime(time.time())
print("present local time",time.strftime('%b %d %Y %H:%M:%S',t))

import calendar
cal=calendar.month(2020,10)
print(cal)