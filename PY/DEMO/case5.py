# coding=utf-8
# 统计给出的txt文本 中的单词个数（纯英文文本）
import re
import sys

def wordNum(filepath):
    text = open(filepath).read( )
    regex=re.compile("(?x) (?: [\w-]+ )")
    words=regex.findall(text)
    return len(words)

print wordNum('F:/PY/license.txt')

# def divide(c, regex):
# #the regex below is only valid for utf8 coding
#     return regex.findall(c)
