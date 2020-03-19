from typing import TextIO

import jieba
import itertools as it
import translators as ts


def permutechisen(s, char):
    if not s:
        return [s]
    binary = it.product(['', char], repeat=len(s) - 1)
    zipped = (it.zip_longest(s, comb, fillvalue='') for comb in binary)
    return [''.join(it.chain.from_iterable(x)) for x in zipped]


def trans(list1):
    mylist = []
    for i in range(len(list1)):
        chi_eng_google = ts.google(list1[i], 'zh-CN', 'en')
        mylist.append(chi_eng_google)
    result = str("/ ".join(mylist)) + '\n'
    return result


print(trans(['如何', '确定', '出生', '顺序']))

fa = open('test.txt', 'a')

# fa.write(trans(['如何', '确定', '出生', '顺序']))


def permutechieng(seg_list):
    for i in range(len(permutechisen(seg_list, ' '))):
        # fa.write(permutechisen(seg_list, '/ ')[i])
        fa.write(trans(permutechisen(seg_list, ' ')[i].split()))


# print(permutechieng(['如何', '确定', '出生', '顺序']))

# print(type(permutechisen(['如何', '确定', '出生', '顺序'], '/ ')[1]))

# fa.write(permutechisen(['how', 'are', 'you', 'doing'], '/ ')[1])

# useful below
# permutechieng(['如何', '确定', '出生', '顺序'])


# print(permutechisen(['如何', '确定', '出生', '顺序'], ' '))
