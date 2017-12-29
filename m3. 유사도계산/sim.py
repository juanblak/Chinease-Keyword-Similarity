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

f = open('noun.txt')
v =open('cat.txt')
g = open('result.txt', 'w')

t1=f.read()
t1 = t1.strip()
t1 = t1.split()

t2=v.read()
t2= t2.strip()
t2 = t2.split()

#【计算前五个】
for n in t1:
    g.write(n.encode('GBK'))
    list=[] #265
    for c in t2:
        y = model.wv.similarity(n.decode('utf-8'),c.decode('gbk')) #!!!!!!!!!
        list.append([c,y])

    list.sort(key=lambda x: x[1],reverse=True)

    for i in range(0,5):
        g.write(' ')
        g.write(list[i][0])
        g.write(' ')
        g.write(str(list[i][1]))

    g.write('\n')


# 【计算大于0.7】
# for n in t1:
#     g.write(n.encode('GBK'))
#     for c in t2:
#         y = model.wv.similarity(n.decode('utf-8'),c.decode('gbk')) #!!!!!!!!!
#         if y > 0.7:
#             g.write(' ')
#             g.write(c)
#             g.write(' ')
#             g.write(str(y))
#
#     g.write('\n')



# 【计算两个词的相似度/相关程度】
# try:
#     y1 = model.similarity(u"饮料", u"男")
# except KeyError:
#     y1 = 0
# print u"【饮料】和【男】的相似度为：", y1
# print"-----\n"

# print(model.similarity(u"饮料",u"年轻"))

# # 【计算某个词的相关词列表】
# y2 = model.most_similar(u"建材市场", topn=20)  # 20个最相关的
# for item in y2:
#     print item[0], item[1]
# print"-----\n"

# # 【计算多个词的相关词列表】
# y3 = model.most_similar([u'饮料', u'年轻'], topn=5)
# for item in y3:
#     print item[0], item[1]
# print"----\n"