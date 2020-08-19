# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:15:31 2020

@author: USER
"""

scores=[]
maxscores=0
minscores=100
total=0
for i in range(5):
    n=int(input('成績'))
    scores.append(n)
    if  n >maxscores:
        maxscores=n
    if n <minscores:
        minscores=n
    total=total+n
s=total/len(scores)
print('總分:',total)
print('平均:',s)
print('最高分:',maxscores)
print('最低分:',minscores)



