import jieba
import itertools as it
import translators as ts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

print("Please input an English question:")
eng_qns = input()

eng_chi_google = ts.google(eng_qns, 'en', 'zh-CN')
print(eng_chi_google)

seg_sentence = list(jieba.cut(eng_chi_google, cut_all=False))


def permutechisen(s, char):
    if not s:
        return [s]
    binary = it.product(['', char], repeat=len(s) - 1)
    zipped = (it.zip_longest(s, comb, fillvalue='') for comb in binary)
    return [''.join(it.chain.from_iterable(x)) for x in zipped]


print(permutechisen(seg_sentence, '/ '))


def trans(list1):
    mylist = []
    for i in range(len(list1)):
        chi_eng_google = ts.google(list1[i], 'zh-CN', 'en')
        mylist.append(chi_eng_google)
    print("/ ".join(mylist))


# prints each chinese sentence with the translated english sentence
def permutechieng(seg_list):
    for i in range(len(permutechisen(seg_list, ' '))):
        print(permutechisen(seg_list, '/ ')[i])
        trans(permutechisen(seg_list, ' ')[i].split())


def trans_join(list1):
    mylist = []
    for i in range(len(list1)):
        chi_eng_google = ts.google(list1[i], 'zh-CN', 'en')
        mylist.append(chi_eng_google)
    result = " ".join(mylist)
    return result


# returns the whole list of translated sentences
def permutechieng_list(seg_list):
    whole_list = []
    for i in range(len(permutechisen(seg_list, ' '))):
        # print(permutechisen(seg_list, '/ ')[i])
        # trans(permutechisen(seg_list, ' ')[i].split())
        whole_list.append(trans_join(permutechisen(seg_list, ' ')[i].split()))
    return whole_list


# print(permutechieng_list(seg_sentence))


def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


# prints the top 'k' sentences with the most sentence difference with the original sentence
def similarity_list(string1, list1):
    mylist = []
    for i in range(len(list1)):
        arr = get_cosine_sim(string1, list1[i])
        mylist.append(np.amin(arr))
    arr = np.array(mylist)
    k = 4  # the top k sentences
    idx = np.argpartition(arr, k)
    for j in range(k):
        print(list1[idx[j]])


similarity_list(eng_qns, permutechieng_list(seg_sentence))

# print(permutechieng(seg_sentence))
