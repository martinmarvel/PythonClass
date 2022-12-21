# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:39:24 2022

@author: omert
"""

print("python classes")
print('new class')

print("İstanbul, İzmir, Ankara")
#%%
#kaçış karakteri "\"
print("İstanbul, \nİzmir,\nAnkara")
#%%
#" "       ''
print('Türkiye\'deki insanlar')
#%%
#karakter birleştirme
print("python eğiitimi")
print("python"+" "+"eğitimi")
#%%
#raw string "r" ters slash olduğu için özel karakter olmadığını belirtmemiz gerek

print(r'C:\User\omert')
#%%
#sayıları konsola yazdırma

print(5)
print(5+6)
print(8/2+40-8)
#%%
#print fonks. parametreleri "end"

print("python", end=" ")
print("eğitimi")

#sep="-"
print("ömer", "talha","özdemir")
print("ömer", "talha","özdemir", sep="-")

# * karakter arası boşluk bırakma
print("tc")
print(*"tc")
print(*"tc", sep=".")
#%%
#format metdounun incelenmesi. stringlere ait bir metoddur

print("İsim: Ömer Talha"
      "Soyad: Özdemir"
      "Doğum: 1988")

print("Adı:{} Soyadı: {} Doğum: {}".format("Ömer Talha", "Özdemir", "1988"))
#%%
#todo yapılackalar listesi hazılayıp ide üzerinden kontrol etemey yarar

#TODO yeni bir giriş fonks. yapılacak
#TODO yapıalcak olan işlerin kontrolü
#%%
#help fonksiyonu, diğer fonks. ların özelliklerini parametrelerini görmemize yarar(dökümantasyon) konsol da gösterir
#fonks. üzeirnde ctrl+ı yazınca da fonks. ile ilgili parametrelere ulaşabiliriz help penceresinde gösterilir

help(print)
