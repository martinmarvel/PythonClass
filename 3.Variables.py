# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:59:08 2022

@author: omert
"""
sayi1 = 144
sayi2 = 156

print(sayi1*67)
#isidentifier() ile değişken adları uygun mu değil mi kontrol edebiliriz.
#%%
#tam sayı değişkenleri "int"
#değişken adı değişşsede, eğer içeriği aynı ise id si(adresi) değişmez
sayi3 = 156
sayi4 = 198

print("toplama", sayi3+sayi4 )
print("çıkarma",  sayi3-sayi4)
print("çarpma", sayi3*sayi4)
print("bölme", sayi3/sayi4)

print(type(sayi3))
print(type(sayi4))

print(id(sayi3))
sayi5 = 156
print(id(sayi5))
sayi5 = 153
print(id(sayi5))
#%%
#kesirli sayı değişkeni(float)

degis1 = 13.3
degis2 = 19.0

print("toplama", degis1+degis2 )

print(id(degis1))
print(type(degis2))
#%%
#str karakter depolarlar

isim = "ömer talha"
soyisim = 'özdemir'

print(isim, type(isim))

#length

print(len(soyisim))

print(isim,soyisim)

#concat
fullName = isim+" "+soyisim
print(fullName)

print(fullName[0], fullName[6])
#%%
#değişkenlerin ram da depolanması ve kontrolü "sys" sistem kütüphanesi
import sys
sayi = 111111111111

print(sys.getsizeof(sayi))

print("195"*2)
print(int("195")*2)


#%%
#kullanıcıdan girdi alma

girdi = input("giriniz:")
print("sonuç:",girdi)

carpma = input("sayıyı girin:")
print("sayının 9 katı", carpma*9)

#%%
print(7 / 2 * 2 + 4 / 4 + 3 ** 2)
