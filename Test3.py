from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

# print("Please input an English question 1:")
# english01 = input()
#
# print("Please input an English question 2:")
# english02 = input()


def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


# arr = get_cosine_sim(english01, english02)
#
# print(np.amin(arr))

list_try = [0.9128709291752769, 0.9999999999999999, 0.9999999999999999, 0.7999999999999999, 0.7302967433402215, 0.47434164902525683, 0.7302967433402215, 0.5477225575051662]

list_try2 = [1, 7, 9, 2, 0.1, 17, 17, 1.5]

A = np.array(list_try)

print(A)

idx = np.argpartition(A, 3)

print(idx)


for i in range(3):
    print(idx[i])

# print(list_try.index(min(list_try)))