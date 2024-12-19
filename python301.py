#FONKSİYONLAR
"""
print("a","b", sep="_")
print(len("a"))

def kare_al(x):
    print("girilen sayının karesi : "+str(x**2))
    
kare_al(3)

def kare_al(x):
    print("girilen sayı  : "+str(x)+" karesi: "+str(x**2))
    
kare_al(3)

#iki argümanlı fonksiyon tanımlama

def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(2,3)

#Ön tanımlı argumanlar

def carpma_yap(x,y):
    print(x*y)

carpma_yap(3) #TypeError: carpma_yap() missing 1 required positional argument: 'y' 



#Arguman sıralama

def carpma_yap(x,y=5):
    print(x*y)
carpma_yap(y=2,x=3)
carpma_yap(2,3)

#tekrar eden işlemleri var olan işlemleri pratik hale getirme için fonksiyonlara ihtiyacımız var

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

direk_hesap(25,40,70)

#çıktıyı kullanmak başka işlemin girdisi olarak kullanmak
#cikti=direk_hesap(25,40,70)
#print(cikti) direk bu şekilde kullanmak mümkün değil 


def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj

cikti=direk_hesap(25,40,70)*9
print(cikti)

#LOCAL VE GLOBAL

x=10 #global kısım
y=20

def carpma_yap(x,y): #local kısım
    return x*y

carpma_yap(2,3)

#Local etki alanından global etki alanını değiştirmek

x=[]
#del x
def eleman_ekle(y):
    x.append(y)
    print(str(y)+" ifadesi eklendi ")
    
eleman_ekle(1)

eleman_ekle("veli")

#KARAR KONTROL YAPILARI
#TRUE FALSE

sinir=5000

print(sinir==4000)
print(sinir==5000)
 
#İF else

sinir=50000
gelir=40000

if gelir>sinir:
    print("gelir sınırdan büyük")
else:
    print("gelir sınırdan küçük")
    
if gelir==sinir:
    print("gelir sınıra esittir")
else:
    print("gelir sınıra eşit değil")

#ELİF
sinir=50000
gelir=60000
gelir2=50000
gelir3=35000
if gelir>sinir:
    print("tebrikler kazandınız")
elif gelir<sinir:
    print("uyarı")
else:
    print("takibe devam")

#MİNİ UYGULAMA
sinir=50000
magaza_adi=input("magaza adı nedir? : ")
gelir=int(input("gelirinzi giriniz :"))

if gelir>sinir:
    print(magaza_adi+" promosyon kazandınız")
elif gelir<sinir:
    print("uyarı çok dusuk geldi : "+str(gelir))
else:
    print("takibe devam")

#DÖNGÜLER FOR

ogrenci=["ali","veli","isik","berk"]

for i in ogrenci:
    print(i)

maaslar=[1000,2000,3000,4000,5000]

for maas in maaslar:
    print(maas*2)

def kare_al(x):
    print(x**2)

kare_al(2)

maaslar=[1000,2000,3000,4000,5000]

#maaslara yüzde 20 zam yapılacak

def yeni_maas(x):
    print(x*20/200+x)

for maas in maaslar:
    yeni_maas(maas)


#if, for ve fonksiyonların birlikte kullanımına yönelik uygulama

maaslar=[1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100+x)
    
def maas_alt(x):
    print(x*20/100+x)

for i in maaslar:
    if i>=3000:
        maas_ust(i)
    else:
        maas_alt(i)


#break & continue

maaslar=[8000,5000,2000,1000,3000,7000,1000]

maaslar.sort()
print(maaslar)

for i in maaslar:
    if i==3000:
        print("kesildi")
        break
    print(i)
print("------------------")
for i in maaslar:
    if i==3000:
        print("kesildi")
        continue
    print(i)
    
"""

#WHİLE
sayi=1

while sayi<10:
    sayi+=1
    print(sayi)


    