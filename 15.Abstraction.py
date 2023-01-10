# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:54:43 2023

@author: omert
"""
from abc import ABC, abstractclassmethod
#Parent class ta kullanlcak bir, örneğin bir ortak metodun, o metodu kullanmak isteyen diğer sucClass larda,
#kullanıldığı class a özel hale gelmesi durumu abstraction diyebiliriz. örn: çalışmak fiili bir insan da, bir içten yanmalı-
#motorda, bir bilgisayarda farklı biçimde meydana gelir. Abstract class ile bu genel anlamda soyut çalışmak fiili,
#kullanılacağı diğer classlarda o class ın ihtiyacı olduğu yöntemle çalışır.
# Bir abstract class miras alındığı zaman, muhakkak onu inherit eden class larda, abstract class ın metodu olmak zorunda


class Makina(ABC):#Makina ABC ile artık bir abstract class
    @abstractclassmethod#abstract classın metodu
    def calis(self):
        print("makine çalıştı")
        
class camasirMakinasi(Makina):
    def calis(self):
        print("çamaşır makine çalıştı")
        
class bulasikMakinasi(Makina):
    def calis(self):
        print("bulaşık makine çalıştı")
        
camasir1 = camasirMakinasi()
bulasik1 = bulasikMakinasi()


camasir1.calis()
bulasik1.calis()

class Insan:
    def camasirYika(self, makina:camasirMakinasi):
        #if makina == camasirMakinasi: nöylede yazabiliriz
        if type(makina) == camasirMakinasi:
            print("insan çamaşır yıkadı")
            makina.calis()        
        else:
            print("burada çamaşır yıkanır")
insan1 = Insan()
insan1.camasirYika(camasir1)
#insan1.camasirYika(bulasik1)#Insan() classı içindeki çaşır yıkama metodu if bloğu ile sadece çamasşıra sabitlendiği için
#artık buulaşık yıkama sub class ı kullanılamaz
