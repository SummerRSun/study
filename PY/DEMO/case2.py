# coding=utf-8
# 给一个年份（四位的字符串）输出该年的天数比如’2013‘ 输出365天
# calendar.monthrange(year,month):返回某个月的weekday的第一天和这个月的所有天数

import calendar
# print calendar.calendar(2016)
def get_year_range(year):
    year_range = 0
    for month in range(1,13):
        monthRange = calendar.monthrange(year,month)
        month_range = monthRange[1]
        year_range = month_range + year_range
        # print "when month is %d , range is %d " %(month,month_range)
        # print "year_range is %d" % year_range
    return year_range
print get_year_range(2013)


