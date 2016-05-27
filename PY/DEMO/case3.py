# coding=utf-8

'''
给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。
'''
import time
time1 = {'year':'2013','month':'9','day':'22','hour':'16','minute':'45','second':'2'}

print time1['year']

year = time1.get('year')
month = time1.get('month')
day = time1.get('day')
hour = time1.get('hour')
minute = time1.get('minute')
second = time1.get('second')

list = []
list.append(year.zfill(4))
list.append(month.zfill(2))
list.append(day.zfill(2))
list.append(hour.zfill(2))
list.append(minute.zfill(2))
list.append(second.zfill(2))
print list

str = '-'.join(list[:3]),':'.join(list[3:])
print str

# ['2013', '09', '22', '16', '45', '02']
# 2013-09-22 16:45:02





