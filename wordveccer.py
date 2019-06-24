from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
import nltk
from nltk.stem import SnowballStemmer
import os
import string
import re

DATA_FOLDER = "data"
stemmer = SnowballStemmer('dutch')
filter = nltk.corpus.stopwords.words('dutch')
filter.extend(string.punctuation)
filter.extend(['"', '...', "¨"])
filter = set(filter)

_digits = re.compile('\d')


def contains_digits(d):
    return bool(_digits.search(d))


with open(os.path.join(DATA_FOLDER, 'corpus.txt'), 'r') as f:
    texts = [
        [re.sub('[^ a-zA-Z]', '', word) for word in doc.lower().split() if word
         not in filter and not contains_digits(word)] for doc in f.readlines() if doc != "\n"
    ]

path = get_tmpfile("data/word2vec.model")

model = Word2Vec(texts, size=100, window=5, min_count=1, workers=4)
model.save("data/word2vec.model")

breakpoint()
