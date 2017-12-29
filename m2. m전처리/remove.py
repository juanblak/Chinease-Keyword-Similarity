# -*- coding: utf-8 -*-
from gensim.models import word2vec
import logging
import multiprocessing

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print "start"
# 主程序
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus("mfullnoun.txt")  # 加载语料
model = word2vec.Word2Vec(sentences,size=0, min_count=0, iter=1, negative=0, workers=multiprocessing.cpu_count())  # 训练skip-gram模型，默认window=5

print model
model.save("remove.model")

g = open('remove.txt', 'w')

for k,v in model.wv.vocab.items():
    g.write(k)
    g.write('\n')

