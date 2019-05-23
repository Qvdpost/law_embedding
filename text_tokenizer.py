import nltk
from nltk.stem import SnowballStemmer
import os
import string
import re
from gensim.models import Word2Vec
from gensim import corpora
from collections import defaultdict

import nl_core_news_sm

DATA_FOLDER = "data"
stemmer = SnowballStemmer('dutch')
filter = nltk.corpus.stopwords.words('dutch')
filter.extend(string.punctuation)
filter.extend(['"', '...', "¨"])
filter = set(filter)

_digits = re.compile('\d')
nlp = nl_core_news_sm.load()


def contains_digits(d):
    return bool(_digits.search(d))

# with open(os.path.join(DATA_FOLDER, 'corpus.txt'), 'r') as f:
#     for doc in f.readlines():
#         doc = [word.lower() for word in doc if word.lower() not in filter and not contains_digits(word)]
#         doc = nlp(doc)
#         print([(w.text, w.pos_) for w in doc])
#         breakpoint()


with open(os.path.join(DATA_FOLDER, 'corpus.txt'), 'r') as f:
    texts = [
        [word.strip('[').strip(']').strip('(').strip(')') for word in doc.lower().split() if word
         not in filter and not contains_digits(word)] for doc in f.readlines()
    ]

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [
    [token for token in text if frequency[token] > 1]
    for text in texts
]

# with open(os.path.join(DATA_FOLDER, 'corpus.txt'), 'r') as f:
#     tokens = nltk.tokenize.sent_tokenize(f.read(), language='dutch')
#     breakpoint()
#
#     tokens = [nltk.tokenize.word_tokenize(token, language='dutch') for
#               token in tokens]
#     breakpoint()
#
#     tokenized = []
#     for sentence in tokens:
#         tokenized.append([word.lower() for word in sentence if word.lower()
#                           not in filter and not contains_digits(word)])

dictionary = corpora.Dictionary(texts)
# dictionary.save('data/gensim.dict')

# model = Word2Vec(tokenized, min_count=1, size=300, workers=4, sg=1)

breakpoint()
