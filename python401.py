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
"""

#FONKSİYONEL PROGRAMLAMA

#YAN ETKİSİZ PROGRAMLAMA PURE

A=9
def impure_sum(b):
    return b+A

def pure_sum(a,b):
    return a+b

print(impure_sum(6))  #dışardan etkilenebiliyor bağımlı 
print(pure_sum(3,4))

