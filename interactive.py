from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec


path = get_tmpfile("data/word2vec.model")

model = Word2Vec.load("data/word2vec.model")

breakpoint()
