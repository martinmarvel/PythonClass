# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 01:25:19 2022

@author: omert
"""

# aynı işellmelerin tekrar tekrar kodlanmasını önlmeye yarar

# parametresiz fonk


from math import sqrt


def bilgileriSoyle():
    print("ömer")
    print("talha")
    tekBilgi()


def tekBilgi():
    print("34")


bilgileriSoyle()
tekBilgi()
# %%
# Parametreli fonks


def topla(sayi1, sayi2):
    print(sayi1 + sayi2)


topla(3, 4)
# %%
# Return kavramı; foks çalıştığında ortaya bir ürün çıkması anlamına gelir


def tekBilgi(yas):
    print(yas)


def tekBilgiReturnIceren(yas):
    return yas


# ürün değişkenine atanan fonks bir değere sahip olsada print içerisinde none gösterdi bunun se-
# fonks sonucunda herhangi bir çıktı dönmedi, dönmesi için return ifadesi kullanmak gerekli
urun = tekBilgi(34)
urunReturnIceren = tekBilgiReturnIceren(55)
print("return içermeyen: ", urun)
print("return içeren: ", urunReturnIceren)


def carp(i1, i2):
    return i1 * i2


carp(8, 89)
# %%
# Return örnek


def mutlakDeger(sayi1, sayi2):
    return abs(sayi1*sayi2)


mutlakDeger(56, 23)
print(mutlakDeger(56, 23)/2)
# birden fazlda değer alan fonks larda değerler return edidliğinde "tuple" olarak return olurlar, liste set vb. şeklindede kullanılabilir


def birdenFazlaDegerOlanFonks(d1, d2, d3):
    return d1, d2, d3


birdenFazlaDegerOlanFonks(44, 33, 66)

# paketi açtık böylece tuple halinden çıkarıp tek tek kullanabildik
b1, b2, b3 = birdenFazlaDegerOlanFonks(44, 33, 66)

print(b1)
print(b2)
print(b3)
# %%
# Pass by value, pass by reference
# tekil değer tutan objeler ile (örn:değişkenler) çoğul değerleri(örn: liste) tutan objlerin davranış biçimleri farklı.

# pass by value
sayi1 = 10
sayi2 = sayi1
print(sayi1, sayi2)
print("---")
sayi1 = 20
print(sayi1, sayi2)

print("---")
print("---")
# pass by reference
liste1 = [10, 20.30, 4]
liste2 = liste1
print(liste1, liste2)
print("---")
liste1[1] = 9
print(liste1, liste2)
# %%
# ARGÜMAN TİPLERİ positional, keyword, default, variable lenght


def topla(s1, s2):  # positional argümana örnek, muhakkak verilmesi geren argumanlar
    return s1+s2


print(topla(3, 3))
print("---")


def topla1(s1, s2=0):  # default argümana örnek, argüman boş verilsede olur defaultu belirtilmiş
    return s1+s2


print(topla1(30))
print("---")
print(topla1(s1=30, s2=34))  # keyword argüman

print("---")


# varaible argument; birden fazla argüman alma
def carpma(k1, k2, *variableLenght, **keywordluArgumanlar):
    print(variableLenght)
    print(sum(variableLenght))
    print(k1+k2)
    print(keywordluArgumanlar)
    return sum(variableLenght) * 4


# ilk iki arg positionla, sonraki variable lenght, sonuncusu keyword lü args
carpma(5, 4, 5, 6, 7, 66, 5, 4, 4, 4, adi="ömer")

# %%
# positional ve dafoult örnek; alttaki örneğere


def kimlikBilgisi(adi, soyadi, yasi="", dogumTarihi=""):
    print("kişinin adı: ", adi)
    print("kişinin soyadı: ", soyadi)
    # eğer bilgiler boş ise gösterme
    if yasi != "":
        print("kişinin yaşı: ", yasi)
    if dogumTarihi != "":
        print("kişinin doğum tarihi: ", dogumTarihi)


kimlikBilgisi("ömer", "talha", 34, 1988)
print("---")
# varsayılanı olan args boş olursa bilgi göndermeyebiliriz
kimlikBilgisi("murat", "genç")
print("---")
# keyword kullanırken arg sırasını karıştırırsak bütün arg ları
kimlikBilgisi(yasi=45, dogumTarihi=1999, adi="hasan", soyadi="almaz")
# keywordleri kullanmamız gerekir çünkü positional olan arg lar keywordlü arg lardan önce gelmek zorundadır
print("---")
kimlikBilgisi("emre", "genç", dogumTarihi=1989, yasi=34)
# %%
# Variable lenght


def goster(positional, default="", *args, **kwargs):  # kendi içinde yer değiştirebilir
    print(positional)
    print(default)
    print(args)
    print(kwargs)


goster("ömer", "talha", 4, 5, 6, tarih="bugün", randevu="bugün 13:30")
print("---")
goster("ömer", 4, 5, 6, tarih="bugün", randevu="bugün 13:30")
# %%


def karakok(*args):
    liste = []
    for sayi in args:
        print(round(sqrt(sayi), 2))
        liste.append(round(sqrt(sayi), 2))
    return liste


karakok(4, 5, 6, 34, 2, 1)
# %%
# LOCAL VE YEREL KAVRAMI
# fonks içindeki değişkenler global keywordü yazılmadığı sürece scope dışından(blok dışından) ulaşamayız
# kontrol yapılarında ise böyle bir durum söz konusu değil
#globals() fonks ile bütün global değişkenlere ulaşabiliriz

sayi = 10


def func1():
    global sayi
    sayi = 20
    print("local sayi:", sayi, "Adres", id(sayi))



print("local sayi:", sayi, "Adres", id(sayi))
func1()
print("local sayi:", sayi, "Adres", id(sayi))

if True:
    y = 50
    print(y)
    
print(y)

print(globals())
print("---")
print(globals()["sayi"])
#%%
#RECURSIVE ITERATIVE FONKS LAR; kendi kendini çağıran fonks lar recursive dir, 
#tekrarlanan fonks lara da iterative dir

def iterFunc():
    for i in range(1,20):
        print(i)
        
iterFunc()
print("---")

def recurFunc(sayi):
    if sayi == -1:
        return None
    print(sayi)
    recurFunc(sayi - 1)
    
recurFunc(5)
#%%
#LAMBDA ananymous(isimsiz) fonks lar; tek seferlik çalışır ve ram de daha az yer kaplar

lambdafonks = lambda sayi:sayi*sayi
print(lambdafonks(26))
print("---")

def kareAl(sayi):
    return sayi*sayi


print(kareAl(6))
print("---")
#istesek fonks larıda değişkene atayabiliriz fakat parantez kullanmadan

atanmisKareal = kareAl
print(atanmisKareal(7))
#%%
#ÖZEL FONKSİYONLAR(HAZIR FONKSİYONLAR) FILTER()     MAP()   REDUCE(); dizilerin içinde filtreleme, haritlama, indirgeme

sayilar = [2,4,-6.0,7,34,67,-5,234]

def pozitifMi(s):
    return s>0


pozitifSayiar = list(filter(pozitifMi, sayilar))
pozitifSayiar1= list(filter(lambda s:s>0, sayilar))
negatifSayiar1= list(filter(lambda s:s<0, sayilar))
negatifSayiar2= [sayi for sayi in sayilar if sayi not in pozitifSayiar1]

print(pozitifSayiar,pozitifSayiar1,negatifSayiar1,negatifSayiar2, sep=" --- ")
#%%
#MAP fonks; dizi içindeki değerlerin haritalanmasını sağlayan bir fonksiyondur
#map fonks listede bulunan herbir eleman üzerinde çalışmak zorunda, filter ise liste-
#içindeki elemanların bazılarını seçip üzerinde işlem yapabilmemizi sağlar

sayilar = [3,6,8,12,-6,-45,-3,-6]

def kareAl(s):
    return s**2

sayilarKaresi2 = list(map(kareAl, sayilar))
sayilarKaresi2 = tuple(map(kareAl, sayilar))

sayilarKaresi3 = list(map(lambda s:s*s, sayilar))
#%%
#REDUCE fonks; indirgemek demek, listemiz içindeki değerleri belirlemiş olduğumuz parametre ile -
#bir sonra ki değer diğer değerler ile beraber gönderilemeye başlıyor
from functools import reduce
sayilar = [3,6,8,12,-6,-45,-3,-6]
#her defasında dizi içindeki elemanları ikişerli elemanlar olarak gönderir

def topla(s1,s2):
    return s1 + s2

toplam = reduce(topla, sayilar)
toplam1 = reduce(lambda s1, s2:s1+s2, sayilar)
#%%
#reduce ve map fonks beraber kullanımu, dönem sonu notu hesaplama
from functools import reduce

katSayilar = [0.2,0.3,0.5]
notlar = [60,40,70]

donemSonuNotlari = list(map(lambda s1,s2 : s1*s2, katSayilar, notlar))

donemSonuNotlari1 = reduce(lambda s1,s2: s1+s2, donemSonuNotlari)

#%%
#ZIP fonks bilgilerin/değerlerin sıkıştırlmasını sağlar

nolar = [1,2,3]
isimler = ["ömer","talha","özdemir"]

ziplenmis = zip(nolar,isimler)

bilgiler = list(ziplenmis)

yaslar = (23,45,67)

bilgiler = list(zip(nolar,isimler,yaslar))
print(bilgiler)
print("---")

for bilgi in bilgiler:
    print("no: {} ad: {} yas: {}".format(bilgi[0],bilgi[1],bilgi[2]))

print("---")

#unpack yapılmış hali
for no, ad, yas in bilgiler:
    print("no: {} ad: {} yas: {}".format(no,ad,yas))
    
print("---")
#sözlük haline getirme
ziplenmis = zip(nolar,isimler)

bilgiler = dict(ziplenmis)
print(bilgiler)
#%%
#ENUMERATE, ALL, ANY FONKS
#enumareta verileri numaralandırmayı sağlar

sayilar = (23,45,67,8988)

print(enumerate(sayilar))

for no, sayi in enumerate(sayilar,4):
    print("{}. {}".format(no,sayi))

print("---")

rehber = {"ömer": 345345, "talha": 45345345, "özdemir": 234535}
print(list(enumerate(rehber,1)))
print(list(enumerate(rehber.values(),1)))


print("---")
#all()#bütün değerler true ise return true
#any()#en az 1 tanesi true ise return true

print(all([True,True,True]))
print(all([True,False,True]))
print("---")

print(any([True,True,True]))
print(any([True,False,True]))
print(any([False,False,False]))
#%%
# Bir fonks nun fonks döndürmesi. bir fonks çalıştırmadan önce başka bir fonks çalıştırma işlemi

def bilgiVer(func):
    print("bilgi veriliyor")
    return func

def kullaniciBilgisiVer(isim):
    return "adı: "+ isim

bilgiVer(kullaniciBilgisiVer)("ömer")
print("---")
#%%
#DECORATORS

def funcInfo(func):
    def bilgileriVer():
        print("fonks çalışması başladı")
        func()
        print("fonks çalışması bitti")
    return bilgileriVer


@funcInfo
def soruSor():
    print("soru sordum")
    
@funcInfo
def cevapVer():
    print("cevap verdim")


#funcInfo(soruSor)()
#funcInfo(cevapVer)()
soruSor()
print("---")
cevapVer()
#%%
# Decorater lerde argüman ileitimi

def funcInfo(func):
    def inner(*args, **kwargs):
        print("konuşma başladı")
        func(*args,**kwargs)
        print("konuşma bitti")
    return inner

@funcInfo
def soruSor(isim, yas, soru, **kwargs):
    print("soru soran kişi:")
    print("adı: {} yaşı: {}".format(isim, yas))
    print("sorusu: {}".format(soru))    
    try:
        print(kwargs["bilgi"])
    except Exception:
        print("bilgi: keywordu gelmedi")
        
@funcInfo
def cevapVer(isim, yas, cevap, **kwargs):
    print("soru soran kişi:")
    print("adı: {} yaşı: {}".format(isim, yas))
    print("cevabı: {}".format(cevap))  
    try:
        print(kwargs["bilgi"])
    except Exception:
        print("bilgi: keywordu gelmedi")


soruSor("ömer", 34, "yaşın kaç", bilgi = "amacı : soru sormak")
cevapVer("talha", 23, "23 yaşındayım")
#%%

from math import sqrt
import time

def calisma(func):
    def inner(*args, **kwargs):
        baslangic = time.time()
        func(*args,**kwargs)
        bitis = time.time()
        print("çalışma süresi: ", bitis-baslangic)
        return inner
 
@calisma 
def kareKokAl(sayilar):
    sayilar = [sqrt(sayi) for sayi in sayilar]
    return sayilar

@calisma     
def kareAl(sayilar):
    sayilar = [sayi ** 2 for sayi in sayilar]
    return sayilar

sayilar = list(range(10000))

kareKokAl(sayilar)



























