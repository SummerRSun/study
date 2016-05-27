# coding=utf-8

# 给你的头像右上角加上数字达到示例图的类似效果
t = {'year':'2013','month':'9','day':'22','hour':'16','minute':'45','second':'2'}

d =[t['year'].zfill(4),t['month'].zfill(2),t['day'].zfill(2),t['hour'].zfill(2),t['minute'].zfill(2),t['second'].zfill(2)]
print d
print '-'.join(d[:3]),':'.join(d[3:])