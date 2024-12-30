#NESNE YÖNELİMLİ PROGRAMLAMA

"""class VeriBilimci():
    print("bu bir sınıftır")
    
#Özellikler

class VeriBilimci():
    bolum=""
    sql="Evet"
    deneyim_yili=0
    bildigi_diller=[]
    
VeriBilimci.bolum
VeriBilimci.sql

#değiştirilebilir
VeriBilimci.sql="hayir"  
print(VeriBilimci.sql)

#Sınıf örneklendirmesi

ali=VeriBilimci()
ali.bildigi_diller.append("python") #tüm sınıfı etkiledi
print(ali.sql)
veli=VeriBilimci()
print(veli.bildigi_diller) #veli python biliyormu ki?

#Örnek özellikleri

class VeriBilimci():
    bildigi_diller=["r","c#"]
    bolum=""
    sql=""
    def __init__(self): #örnekleri temsil ediyor
        self.bildigi_diller=[]
        self.bolum=""

ali=VeriBilimci()
print(ali.bildigi_diller)

veli=VeriBilimci()
print(veli.bildigi_diller)

ali.bildigi_diller.append("python")
veli.bildigi_diller.append("c++")

print(ali.bildigi_diller)
print(veli.bildigi_diller) #bu yapılan örnek özellği tanımlamaktır

#print(VeriBilimci.bildigi_diller)  AttributeError: type object 'VeriBilimci' has no attribute 'bildigi_diller' hiçbir özelliği yok.

print(VeriBilimci.bolum)
ali.bolum="istatistik"
print(VeriBilimci.bolum)
veli.bolum="matematik"
print(veli.bolum)
print(ali.bolum)
print(VeriBilimci.bolum)

#Örnek Metodları

#Her bir veri bilimcinin yeni öğrendiği dili diğer bilgiği dillere eklesin

class veribilimci():
    calisanlar=[]
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=""
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
        
feyza=veribilimci()
print(feyza.bildigi_diller)
print(feyza.bolum)

sude=veribilimci()
print(sude.bildigi_diller)
print(sude.bolum)

#veribilimci.dil_ekle("R") VAR OLAN YAPI ÜSTÜNE BİR ŞEY EKLENMEZ
feyza.dil_ekle("R")
print(feyza.bildigi_diller)

sude.dil_ekle("python")
print(sude.bildigi_diller)


#MİRAS YAPILARI (İNTHERİTANCE)

class calisanlar():
    def __init__(self):
        self.adi=""
        self.soyad=""
        self.adres=""
        
class veribilimci(calisanlar):
    def __init__(self):
        self.programlama=""

veribilimci1=veribilimci()
veribilimci1.adi


class pazarlama(calisanlar):
    def __init__(self):
        self.hikayeAnlatici=""

pazarlamaci1= pazarlama()
pazarlamaci1.hikayeAnlatici

class calisanlar_yeni():
    def __init__(self,adi,soyad,adres):
        self.adi=adi
        self.soyad=soyad
        self.adres=adres

feyza=calisanlar_yeni("feyza","gökçe","cc")
print(feyza.adi)
print(feyza.soyad)
print(feyza.adres)


#FONKSİYONEL PROGRAMLAMA

#YAN ETKİSİZ PROGRAMLAMA PURE

a=5

def impure_sum(b): #saf olmayan dışardan bağımlı
    return b+a


def pure_sum(a,b): #saf olmayan dışarıya bağımlı değil
    return a+b

print(pure_sum(3,4))
print("-----------------------------")
print(impure_sum(6))

#Ornek 2

class sayac:
    def __init__(self,filename):
        self.file=open(filename,'r')
        self.lines=[]
        
    def read(self):
        self.lines=[line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
s=sayac("deneme.txt")

print(s.lines)
print(s.count())


s.read()

print(s.lines)
print(s.count()) #ilk başta lines boş bir liste bu yüzden count metodu 0 dönüyor ama read eklenince dosyaı okuyor ve listeye kaydediyor liste dolu olduğundan count metoduda değişiyor ve nesnenin durumu değişmiş oluyor.

#girdi verdiğinde çıktı üretebilenler fonksiyonel programlardır.



#İsimsiz Fonksiyonlar

def old_sum(a,b):
    return a+b

print(old_sum(8,4))

new_sum=lambda a,b:a+b
print(new_sum(2,6))

z_list=[('b',3),('a',8),('d',12),('c',1)]
print(z_list)

print(sorted(z_list,key=lambda x:x[1])) #ÇOKKKK ÖNEMLİİİİİ



#Vektorel Operasyonlar

a=[1,2,3,4]
b=[2,3,4,5]

ab=[]

range(0,len(a))

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

print(ab)

import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

print(a*b)

#map filter reduce

liste=[1,2,3,4,5]

for i in liste:
    print(i+10)

print(list(map(lambda x:x*10,liste)))

#filter
print("----------------")
aliste=[1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x:x%2==0,aliste)))

#reduce indirgemek

from functools import reduce

bliste=[1,2,3,4]
print(reduce(lambda a,b:a+b,bliste))

#fonksiyonel programlamada işlerimizi kolaylaştıran daha az yan etsisi olan ve daha az problem oluşturan programlardır.



#MODUL OLUŞTURMAK

import hesapModulu as hm

hm.maas(78)

from hesapModulu import maas
maas(4000)

import hesapModulu as hm
hm.maaslar
"""

#HATALAR İSTİSNALAR

#ZeroDivisionError
a=10
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("payda da sifir olmaz")

#Tip hatasi

a=10
b="5"

try:
    print(a+b)
except TypeError:
    print("tip hatasi")