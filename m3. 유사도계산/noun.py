# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


f = open('remove.txt')
v=open('vocab.txt')
g = open('noun.txt', 'w')

t1=f.read()
t1 = t1.strip()
t1 = t1.split()

t2=v.read()
t2 = t2.strip()
t2 = t2.split()

for n in t1:
    for v in t2:
        # print n,v
        if n==v:
            g.write(n)
            g.write('\n')
            # print n,'yes'

            continue