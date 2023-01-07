# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 07:08:39 2023

@author: omert
"""

sayi = 5

print(isinstance(sayi, int))
print(isinstance(sayi, float))
print("---")

help(list)
print("---")
print(issubclass(list, object))
# %%
# Metodlarnı çözümlenme sırası MRO


class A:
    def metot1(self):
        print("a metot 1")

    def metot2(self):
        print("a metot 2")


class B(A):
    def metot3(self):
        print("b metot 3")

    def metot4(self):
        print("b metot 4")


class C(B):
    def metot5(self):
        print("c metot 5")

    def metot1(self):
        print("c metot 1")
# __init__ metodu oluşturmazsak otomatik olarak arka planda kendi oluşur


aObjesi = A()
bObjesi = B()
cObjesi = C()

cObjesi.metot1()
# hem a hem de c sınıfında aynı isimli metod var, önce c sınıfında ki metod çalıştırılır
print("---")
C.mro()  # metotların çalışma sırasını incelemeye yarar

# A super class(parent)
# B sub class(child)

# B -> A yı miras alırsa; single level inheritance(kalıtım)
# C -> B -> A c nin b yi b nin ise a yı miras almasına multi level inheritance
# C -> (B,A) c hem b hem de a dan(birden fazla class) dan miras lırsa multiple level inheritance
# %%
# MRO örnek


class X:
    def metot1(self):
        print("x metot 1")


class Z:
    def metot1(self):
        print("z metot 1")


class Y:
    def metot1(self):
        print("y metot 1")


class A(X, Y):
    def metot1(self):
        print("a metot 1")


class B(Y, Z):
    def metot1(self):
        print("b metot 1")


class C(B, A, Z):
    def metot1(self):
        print("c metot 1")


c1 = C()

print(C.mro())
# %%
# super () fonks., constructor kalıtımı


class A:
    def __init__(self):
        print("a cons")

    def metot1(self):
        print("a metot 1")


class B(A):
    def __init__(self):
        print("b cons")

    def metot1(self):
        print("b metot 1")


class C(B, A):
    def __init__(self):
        print("c cons")
        super().__init__()
        B.__init__(self)
        A.__init__(self)

    def metot1(self):
        print("c metot 1")
        super(B, A).metot1()  # çalışmıyor


ce1 = C()
C.mro()
# %%


class Genel:
    def __init__(self, baslik, icerik, gorsel):
        self.baslik = baslik
        self.icerik = icerik
        self.gorsel = gorsel

    def bilgileriGoster(self):
        print(self.baslik, self.icerik, self.gorsel)
        

        
        

class Spor(Genel):
    def __init__(self, baslik, icerik, gorsel,video):
        super().__init__(baslik, icerik, gorsel)
        self.video = video
        
    def bilgileriGoster(self):
        super().bilgileriGoster()
        
    def videoGoster(self):
        print(self.video, "video oynatııyor")
            
        
        
        
class Finans(Genel):
    def __init__(self, baslik, icerik, gorsel, dovizKurları):
        super().__init__(baslik, icerik, gorsel)
        self.dovizKurları = dovizKurları
        
    def bilgileriGoster(self):
        super().bilgileriGoster()
        self.kurBilgisi()
           
        
    def kurBilgisi(self):
        for dovizAdi, dovizDegeri in self.dovizKurları.items():
            print(dovizAdi,":",dovizDegeri)
    
    def kurGuncelle(self, dovizKurları):
        self.dovizKurları = dovizKurları
   
s1 = Spor("Fener-Galataray", "DErbinin galibi belli oldu", "gorsel.png", "video.mp4")

f1 = Finans(dovizKurları={"dolar": 18.70, "euro": 20, "sterlin": 22.20}, baslik = "dövizde dalgalanma sürüyor", icerik="dövizin seçim sonuna kada baskılanacağı ön görüsü devam etmemkte",gorsel = "gorsel4")

s1.bilgileriGoster()
print("---")
f1.bilgileriGoster()
print("---")
f1.kurBilgisi()
guncelKur = dovizKurları={"dolar": 14.70, "euro": 18, "sterlin": 19}
f1.kurGuncelle(guncelKur)
print("--- kur güncellendi")
f1.kurBilgisi()
print("--- haberin son hali")
f1.bilgileriGoster()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
