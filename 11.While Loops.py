# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 06:27:01 2022

@author: omert
"""
# FOR DÖNGÜSÜ
# for aynı zamanda foreach demek yani her bir eleman için o döngünün bloğu çalışıyor

for i in range(4):
    print("{}. yazı ömer".format(i + 1))


print("---")
for sayi in range(5, 10):  # [5,10]
    print(sayi)
    print("deneme")

# döngü her çalıştığında isim değişkeni, liste içindeki isimleri/elemanları teker teker içerisine almış almış oluyor
print("---")
isimler = ["ömer", "talha", "özdemir"]
for isim in isimler:
    print(isim)

# değişken isimlendirme önemli burada "eleman" dedik yukarıdaki örenkte ise isim kullandık, okuması daha kolay olur
print("---")
tup = (5.0, "ömer", {1: "talha"})
for eleman in tup:
    print(eleman)
# %%
# WHILE DÖNGÜSÜ
# for dan farkı döngünün tamamını biz kontrol ederiz. bir başlangıç ve bitiş değerini biz belirleriz

# initialization
# condition
# increment/decrement
i = 1  # initialization
while i <= 10:  # condition
    print(i)
    i += 1  # increment/decrement
    print("döngü tamamlandı")

# WHILE ÖRNEK
print("---")

sayilar = [12, 44, 56, 33, 34, 7867, 98]

index = 0
while index <= 5:
    print(sayilar[index])
    index += 1

print("---")
print("tersten yazdırma")

index = 5
while index >= 0:
    print(sayilar[index])
    index -= 1
# eleman saysısı dinamik ise

print("elemanlar dinamik ise eleman listeleme")
index = 0

while index < len(sayilar):
    print(sayilar[index])
    index += 1


print("elemanlar dinamik ise elemanları tersten listeleme")
index = len(sayilar)-1

while index > 0:
    print(sayilar[index])
    index -= 1

print("---")
# 5 ve 7 ye bölünebilen sayılar
baslangic = 5
i = baslangic
bitis = 17
sayi1 = 5
sayi2 = 7

sayac = 0
while i <= bitis:
    if i % sayi1 == 0 or i % sayi2 == 0:
        print(i)
        sayac += 1
    i += 1

print("{} ve {} arasında {} ve {} e bölünebilen {} sayı vardır".format(
    baslangic, bitis, sayi1, sayi2, sayac))

# %%
# iki boyutlu bir şekli konsola yazdırma İÇİÇE DÖNGÜ
"""
##########    
##########    
##########    
##########    
##########    
##########    
##########    
##########
"""
satirSayisi = 19
sutunSayisi = 9

satir = 0
while satir < satirSayisi:
    sutun = 0
    while sutun < satirSayisi:
        print("$", end="")
        sutun += 1
    print()
    satir += 1
#%%
# Girilen sayının sayıdeğeri toplamını bulan program


sayi = int(input("sayı griniz: "))   

orjSayi = sayi
sayiDegerleriToplami = 0
sayiDegerleri = []

while sayi > 0:
    sayiDegerleriToplami += sayi %10
    sayiDegerleri.append(sayi % 10)
    sayi //= 10
print(sayiDegerleriToplami)
print(*sayiDegerleri)
print(orjSayi)
print(sum(sayiDegerleri))
#%%
#Faktoriyel hesabı

n = int(input("sayı griniz: ")) 

if n >= 0:
    i = 2
    sonuc = 1
    while i <= n:
        sonuc *= i
        i += 1
    print(n,sonuc)
else:
    print("doğal sayı girmediniz")














