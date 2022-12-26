# -*- coding: utf-8 -*-
"""


@author: omert
"""

# Koşullu İfadeler; ":" bir blok açıldığını temsil eder. İntendetion(boşluk) kurallarına dikkat etmemiz gerkir
# her bloğun 4 space içermesi best practice dir
if True:
    print("if bloğu içinde")
print("---")
# output boş çıkar
anahtar = False
if anahtar:
    print("if bloğu içinde")
else:
    print("if bloğu dışında")

print("---")

if 3 < 4:
    print("3 4 ten küçüktür")
elif 4 > 3:
    print("4 3 ten küçüktür")
else:
    print("yukarıdaki şartlar false olursa çalışır")
# %%
# ÖRNEK

yas = int(input("yaşınızı girin: "))

if yas < 18:
    print("reşit değil")
else:
    print("reşit")
print("---")
# ya da if sayi % 2: çünkü bool casting yapar
sayi = int(input("sayı giriniz"))

if sayi % 2 == 1:
    print(sayi, ":sayısı tektir")
else:
    print(sayi, ":sayısı çifttir")
# %%
# nested conditions

vize = 80
final = 40

if final >= 50:
    ort = vize * 0.4 + final * 0.6
    if ort >= 50:
        print("geçti", ort)
else:
    print("kaldı", final)

# %%
ay = input("ayı girin: ")

if ay == "aralık" or ay == "ocak" or ay == "şubat":
    print(ay, "kış ayıdır")
elif ay == "mayıs" or ay == "haziran" or ay == "temmuz":
    print(ay, " yaz ayıdır")
else:
    print("öyle bir ay yok")
# %%
# hatalı girdi kontrolü

cinsiyet = input("cinsiyet girin: ")
yeniCinsiyet = cinsiyet

if yeniCinsiyet == "erkek" or yeniCinsiyet == "kadın":

    boy = int(input("boyu girin: "))
    yeniBoy = boy

    if yeniBoy <= 30 or yeniBoy >= 199:
        print("Boy değeri 30cm den küçük ve 199cm den büyük olamaz")

    else:
        if yeniCinsiyet == "erkek" and yeniBoy >= 170 or yeniCinsiyet == "kadın" and yeniBoy >= 160:
            print("ön elemeyi geçtiniz")
        else:
            print("ön elemeyi geçemediniz")
else:
    print("Lütfen cinsiyet kısmına 'erkek' ya da 'kadın' cinsiyetlerini giriniz")

    # %%
    # yukarıdaki kod bloğunu 2 satır daha az halini yazdım

    cinsiyet = input("cinsiyet girin: ")

    if cinsiyet == "erkek" or cinsiyet == "kadın":

        boy = int(input("boyu girin: "))

        if boy <= 30 or boy >= 199:
            print("Boy değeri 30cm den küçük ve 199cm den büyük olamaz")

        else:
            if cinsiyet == "erkek" and boy >= 170 or cinsiyet == "kadın" and boy >= 160:
                print("ön elemeyi geçtiniz")
            else:
                print("ön elemeyi geçemediniz")
    else:
        print("Lütfen cinsiyet kısmına 'erkek' ya da 'kadın' cinsiyetlerini giriniz")
        # %%
        # ÖRNEK en büyük ve en küçük sayıyı bulma
        # birden fazla input isterken yan yana yazmak gerekir yada ilk satırın sonun "\" koymak gerekir
sayi1, sayi2, sayi3 = int(input("1.sayıyı girin: ")), int(
    input("1.sayıyı girin: ")), int(input("1.sayıyı girin: "))

print(sayi1, sayi2, sayi3)

sayilar = [sayi1, sayi2, sayi3]

print("liste içindeki en küçük sayu", min(sayilar))
print("liste içindeki en küçük sayu", max(sayilar))
# %%
# ÖRNEK; kullanıcı adı ve şifre kontrolü

kullanıciAdi = "ömer"
kullanıciSifre = "3433"

kullanici = input("adınızı girin: ")
sifre = input("sifre: ")

if kullanici == kullanıciAdi and sifre == kullanıciSifre:
    print("başarılı giriş")
elif kullanici == kullanıciAdi:
    print("şifrenizi doğru giriniz")
else:
    print("böyle bir kullanıcı yok")
# %%
# ÖRNEK; üçgen bilgisini söyleyen program

kenar1, kenar2, kenar3 = int(input("1. kenar değeini giriniz")),\
    int(input("1. kenar değeini giriniz")),\
    int(input("1. kenar değeini giriniz"))

if abs(kenar1 - kenar2) < kenar3 and kenar3 < kenar1 + kenar2:
    if kenar1 == kenar2 and kenar1 == kenar3:
        print("eş kenar")
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        print("ikizkenar")
    else:
        print("çeşitkenar")
# %%
# ÖRNEK; ASCII karakter ile büyük harf küçük harf kontrol

harf = input("lütfen bir harf giriniz: ")

if len(harf) == 1:
    if ord(harf) >= 65 and ord(harf) <= 90:
        print("{} büyük harftir".format(harf))
    elif ord(harf) >= 97 and ord(harf) <= 122:
        print("{} küçük harftir".format(harf))
    else:
        print("lütfen bir harf girin")
