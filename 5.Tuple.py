# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 21:11:29 2022

@author: omert
"""

#Tuple elemanlarına erişmek

tup1 = (15,26,17,25.178)

print(tup1[0])
print(tup1[2])
print(tup1[2:]) # nci elemanından başla listenin sonuna kadar yaz
print(tup1[::2]) # 0 dan başla sonuna kadar git, 2 şer index atlayarak git
print(tup1[-1:0:-1]) # sondan başla, 0 ncı elemana kadar bir bir git (15 gelmez)
#%%
# Tuple metotları

tup = (15,26,17,25.178,26,26)

print(tup.count(26))#vermiş olduğumuz değerden kaç tane olduğunu gösterir output:3
print(tup.index(17))# hangi index te olduğunu söyler
