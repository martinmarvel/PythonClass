# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:30:17 2023

@author: omert
"""

# yineleyeci demek

class ilkYuzSayi:
    def __init__(self):
        self.sayi = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.sayi < 100:
            sayi = self.sayi
            self.sayi += 1
            return sayi
        raise StopIteration
        
        
        
sayilar = ilkYuzSayi()

for i in range(200):
    print(next(sayilar))
    
#bu örnek yukarıdaki örneğin otomatize edilmemiş hali, class ve magic metotları kullanılarak 
#belli bir sayının üzerinde döngüyü kabul etmeyen kıran bir program yazmış olduk yukarıdaki örnekte


sayilar1 = [1,2,3]

sayilar1 = iter(sayilar1)

print(next(sayilar1))
print(next(sayilar1))
print(next(sayilar1))
#print(next(sayilar1)) bu kod çalıştığında StopIteration otomatik olarak devreye girdi
