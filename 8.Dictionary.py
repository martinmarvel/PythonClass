# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 02:07:16 2022

@author: omert
"""

# mutable dır, sıra numarası yok, key vardır
#dict()    {}
sozluk = {1:"ömer",2:"talha",3:"özdemir"}
print(sozluk)

print("2 nolu sözlük elemaı: ",sozluk[2])
print(sozluk.get(5, "ups bulalamadım"))#get kullandığımızda aradığımız anahtar eğer yoksa çıktı alabiliyoruz

bosSozluk1 = {}
bosSozluk2 = dict()
print(bosSozluk1,bosSozluk2)

anahtarlar = [1,2,3]
degerler = ["a","b","c"]
sozluk2Elemanları = zip(anahtarlar,degerler)#anahtar ve elemanları ayrı ayrı oluşturmanın 1. yolu "zip"
#print(*sozluk2Elemanları)# "*" anlamı ziplediklerimizi çıkarmış olmak, çıkardıktan sonra kullanmış oluruz ve içi boşalır
print(dict(sozluk2Elemanları))#içi boşalmadı!!
sozluk2 = dict([(1,"a"),(2,"b"),(3,"c")])#anahtar ve elemanları ayrı ayrı oluşturmanın 2. yolu 
print(sozluk2)
#%%
# ekleme, silme güncelleme

ogrencilerDers = {"ömer":"python", 
                  "talha":{"matematik","data science"}, 
                  "özdemir":{"java","javascript"}, 
                  "yunus":[{"ders adı":"sql", "ders hocası": "mahmut yılmaz"},
                           {"ders adı":"nosql", "ders hocası": "yusuf min"}]}
#print(ogrencilerDers)
print(ogrencilerDers["ömer"])
print(ogrencilerDers["talha"])
print(ogrencilerDers["yunus"])
print(ogrencilerDers["yunus"][1]["ders adı"])
print(ogrencilerDers["yunus"][0]["ders hocası"])

baskasozluk = ogrencilerDers.copy()#yukarıdaki sözlüğün koyasını alıp üzerinde değişklik yatık
baskasozluk["talha"] = "fizik"
print(baskasozluk)

degersizSozluk = dict.fromkeys(["an1","an2","an3"],"varsayılan değer")#default değer için ikinci parametre ekle
print(degersizSozluk)

print(ogrencilerDers.get("özdemir"))
print(baskasozluk.get("özde","böyle bişiy yok"))#eğer elaman yoksa varsayılan mesaj döndürme

print(ogrencilerDers.items())#tuple halinde verir
print(ogrencilerDers.keys())#
print(ogrencilerDers.values())#

ogrencilerDers.pop("ömer")
print(ogrencilerDers)

ogrencilerDers.popitem()#son giren ilk çıkar
print(ogrencilerDers)
#%%
yeniogrencilerDers = {"ömer":"python", 
                  "talha":{"matematik","data science"}, 
                  "özdemir":{"java","javascript"}, 
                  "yunus":[{"ders adı":"sql", "ders hocası": "mahmut yılmaz"},
                           {"ders adı":"nosql", "ders hocası": "yusuf min"}]}



yeniogrencilerDers.setdefault("talha","ers")#default değerini değiştirdik
print(yeniogrencilerDers)
print("-------------------")
yeniogrencilerDers.setdefault("ömer","haylaz ders")#default değerini değiştirdik
print(yeniogrencilerDers)
s1 = {"mirok":"spor"}
yeniogrencilerDers.update(s1)
print(yeniogrencilerDers)


print(bool(0))

















