# coding=utf-8
'''
1.随机输出20个邀请码，要求：
      a.邀请码由大小写字母和数字组成
      b.每个邀请码长度为10
'''

import random,string

def generate_code():
    code_list = []
    # 0-9 数字
    # for i in range(10):
    # # 0-9数字
    #      code_list.append(str(i))

    # A-Z
    for j in range(65,91):
        code_list.append(chr(j))
    # a-z
    for k in range(97,123):
        code_list.append(chr(k))

    slice = random.sample(code_list,10)
    # return slice
    print slice
    str = ''.join(slice)
    return str

def generate(num):
    for i in range(num):
        code = generate_code()
        print code

# if __name__ == '__main__':
generate(20)
