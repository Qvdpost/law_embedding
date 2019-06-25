from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
import nltk
from nltk.stem import SnowballStemmer
import os
import string
import re
import sys

sys.path.append("../")

DATA_FOLDER = "../data/txt_cases"
stemmer = SnowballStemmer('dutch')
filter = nltk.corpus.stopwords.words('dutch')
filter.extend(string.punctuation)
filter.extend(['"', '...', "¨"])
filter = set(filter)

_digits = re.compile('\d')


def contains_digits(d):
    return bool(_digits.search(d))


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        file_count = len(os.listdir(self.dirname))
        for count, fname in enumerate(os.listdir(self.dirname)):
            print(
                f"File {count}/{file_count} ({round((count/file_count * 100), 2)}%): {fname}")
            for line in open(os.path.join(self.dirname, fname)):
                text = [re.sub('[^ a-zA-Z]', '', word) for word in line.lower().split() if word
                        not in filter and not contains_digits(word)]
                yield text


sentences = MySentences(DATA_FOLDER)  # a memory-friendly iterator
# with open(os.path.join(DATA_FOLDER, 'corpus.txt'), 'r') as f:
#     texts = [
#         [re.sub('[^ a-zA-Z]', '', word) for word in doc.lower().split() if word
#          not in filter and not contains_digits(word)] for doc in f.readlines() if doc != "\n"
#     ]


path = get_tmpfile("data/word2vec.model")

model = Word2Vec(sentences, size=25, window=5, min_count=1, workers=4)
model.save("../models/word2vec.model")

breakpoint()
