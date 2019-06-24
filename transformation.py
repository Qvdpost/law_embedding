from gensim import corpora
from gensim import models
from gensim import similarities
import os

if (os.path.exists("data/gensim.dict")):
    dictionary = corpora.Dictionary.load('data/gensim.dict')
    corpus = corpora.MmCorpus('data/gensim.mm')
    print("Used files generated from first tutorial")
else:
    exit('files not found')

# tfidf = models.TfidfModel(corpus)  # step 1 -- initialize a model
#
# corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

with open('data/corpus.txt') as f:
    doc = f.readlines()[0]

vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]  # convert the query to LSI space

index = similarities.MatrixSimilarity(lsi[corpus])  # transform corpus to LSI space and index it
index.save('data/gensim.index')

index = similarities.MatrixSimilarity.load('data/gensim.index')

sims = index[vec_lsi]

sims = sorted(enumerate(sims), key=lambda item: -item[1])

breakpoint()
