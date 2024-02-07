"""
Created by Ignorant on 024/2/6
Description: Module datetime
"""
import datetime

today = datetime.date.today()
# datetime.date.ctime(self): Return ctime() style string.
print(datetime.date.ctime(today))

time_delta = datetime.timedelta(hours=2)
now = datetime.datetime.now()
print(now - time_delta)
