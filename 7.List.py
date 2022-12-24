# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 22:31:39 2022

@author: omert
"""

#List() ya da [] ile oluşturbiliriz

liste = list([1,5,7,8,3])
liste1= [4,6,7,3,2] 
print(liste)
liste1[2] = 100 # liste elamanı değiştirme
print(liste1)
#%%
#liste elemanlarına erişmek

print(liste[4])
print(liste[1:4])
print(liste[1:4:2])# 1 den şla 4 e kadar 2 şer atlayarak geir
print(liste[len(liste)-1])#listenin son elemanına ulaşmak
print(liste[-1])#listenin son elemanına ulaşmak

print(liste[0])#listenin ilk elemanına ulaşmak
print(liste[-len(liste)])#listenin ilk elemanına ulaşmak

print(liste[::2])# listenin başından sonuna kadar 2 ser 2ser atlayarak git
#%%
#listelerde ekleme, güncellme, silme
isimler = ['ömer','talha', 'özdemir']
yaslar = [22,17,34]


isimler = isimler + ["mehmet"]#ekleme
print(isimler)

isimler[1] = "yavuz"#güncelleme
print(isimler)

isimler[1:3] = "melike", "hasan", "yasin" #toplu güncelleme
print(isimler)
isimler[1:3] = ["melike", "hasan", "yasin"] #toplu güncelleme
print(isimler)

del isimler[2]#silme
print(isimler)
#%%
#liste metotları

isimler = ['ömer','talha', 'özdemir']
yaslar = [22,17,34]

karisikListe = isimler + yaslar
print(karisikListe)

#bir objenin yanına "." işareti konulunca onunla ilgili metotlar çıkar
karisikListe.extend({14.7,3,"ömer",None, True, 5+3j})# varolan listeye karışık veri tipinde elamanlae eklendi
print(karisikListe)

karisikListe.index(None)#listede bulunan bir elemanın index numarasını buldu 
print(karisikListe.index(None))
"""
karisikListe.index("m") #varolan listede böyle eleman olmadığı için hata döndürür
print(karisikListe.index("m"))
"""

karisikListe.append("naber")#listenin sonuna eleman ekledi
print(karisikListe)

karisikListe.insert(6, False)#varolan listenin istediğimiz bir yerine eleman ekledi
print(karisikListe)

karisikListe.pop()#liste sonundan eleman çıkarma
print(karisikListe)
karisikListe.pop(7)#listenin herhangi biryerinden eleman çıkarma
print(karisikListe)

karisikListe.remove(22)#verilen elamanı silme
print(karisikListe)

karisikListe.reverse()#listeyi ters çevirme; orjinal listemiz ters çevrilmiş olur 
print(karisikListe)

karisikListe.sort()#küçükten büyüğe sıralar
print(karisikListe)
#%%
#Çok boyutlu listeler(tuple,set, sözlük de de aynı mantık açlışır)

isimler = ['ömer','talha', 'özdemir']
yaslar = [22,17,34]

bilgiler = [["ömer", 22],["talha",17],["özdemir",34]]

print(bilgiler[0])
print(bilgiler[1])
print(bilgiler[2])

print("1. elemanın ismi: ",bilgiler[0][0])
print("1. elamnın yaşı: ",bilgiler[0][1])
print(bilgiler[1][1])
print(bilgiler[2][1])

bilgiler = [({185:"ömer"},{123:"talha"}),("ist","ank")]#tuple içinde sözlük 

print(bilgiler[0])
print("1. indexin 1. elemanı: ",bilgiler[1][1])
print("0. indeksin 1. elemanı: ",bilgiler[0][1])
print(bilgiler[0][0][185])
print(bilgiler[0][1][123])
print(bilgiler[1][0])





















