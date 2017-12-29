# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

num = int(sys.argv[1])

for i in range(0, num):
    snum = str(i + 1)

    f = open('./books_result/' + snum + '.txt')
    g = open('./text/' + snum + '.txt', 'w')

    txt = f.read()
    txt = txt.strip()
    t = txt.split()

    print i + 1

    for x in t:
        x = x.strip()
        g.write(x)
        g.write('\n')
