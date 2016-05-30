# coding=utf-8
# 统计给出的txt文本 中的单词个数（纯英文文本）
import re

def wordNum(filepath):
    text = open(filepath).read( )
    regex=re.compile("(?x) (?: [\w-]+ )")
    words=regex.findall(text)
    return len(words)

print wordNum('E:/PycharmProjects/license.txt')

