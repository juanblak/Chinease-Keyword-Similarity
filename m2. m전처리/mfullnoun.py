# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

g = open('fullnoun.txt', 'w')

# num = int(sys.argv[1])

f = open('./text/1.txt')#원하는 소설파일을 선택

try:
    txt = f.read().decode('gbk')
    t = txt.split()


    for x in t:
        j = 0
        w = ''
        while (j < len(x) and x[j] != '/'):
            w += x[j]
            j = j + 1

        if (j < len(x) and x[j + 1] == 'n'):
             # print(w)
            g.write(w.encode('utf-8'))
            g.write('\n')


except UnicodeDecodeError:
    print ' error!'


