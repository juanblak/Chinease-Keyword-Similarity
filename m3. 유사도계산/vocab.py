# -*- coding: utf-8 -*-
from gensim.models import word2vec

import logging
import multiprocessing
import pandas as pd

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# print "Model:"
model =word2vec.Word2Vec.load('word2vec_wx')
print model

g = open('vocab.txt', 'w')

for k,v in model.wv.vocab.items():
    g.write(k)
    g.write('\n')