# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:21:30 2022

@author: omert
"""

"""
İçerisinde bir değer taşıyan veri tipleri;

NonoType
Numeric
int, float
bool
complex

İçerisinde birden fazla değer taşıyan veri tipleri

List
Tuple
Set
String
Range
Dictionary 
"""

# NoneType: tipi olmayan, başka dillerde "null"

sehir = None
#Numeric
# int ve float

x = 10
y = 10.7
#%%
#bool

key1 = True
key2 = False
k1 = 3<4
key3 = bool(10)
key4 = bool(0)
key5 = bool(-1)
#%%
#complex

ks1 = 2 + 3j
ks2 = complex(4,5)
toplam = ks1 + ks2
#%%
# tuple; immutable yani değiştirelemez, sadece okunabilir, () ile oluşturulur

liste1 = [2,4,7,10]
tuple1 = (7,8,11,-5)
tuple2 = tuple("ömer")#dnüştürme işlemi

liste1[0] = 14
print("tuple elemanı",tuple2[3])
#tuple1[3] = 2  değiştirelemedi
print(liste1, tuple1, tuple2)
#%%
#String veri tipi; immutabledır değiştirelmez, elemaların sıra numarası var
karakter1 = "ömer"
karakter2='talha'
#%%
#Range veri tipi(aralık veri tipi) !!range belirlendikten sonra list, tuple vb. veri tiplerine dönüştürebiliyoruz
#range(start=0,stop,step=1)

aralik = range(10)
print(aralik)
print(*aralik)# * range içindeki değerlere ulaşmaya yarıyor
print(list(aralik))
print(tuple(aralik))
print(set(aralik))

print(*range(1,15,3))# 1 den 15 e kadar 3 er 3 er arttır
print(*range(18,2,-5))# 18 den 2 e kadar 5 er 5 er azalt








































