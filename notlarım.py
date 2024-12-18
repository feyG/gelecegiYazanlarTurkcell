'''a="geleceği yazanlar"
print(a)
print(len(a))
print("---------------")
print(a.upper())
print(a.lower())
print("---------------")
print(a.islower())
print(a.isupper())
print("---------------")
print(a.replace("e","a"))
print(a.replace("e","7"))
print("---------------")
b="  Turkcel Akademi  "
c="678Feyza678Nur678GÖKÇE678"
print(b)
print(b.strip())
print(c.strip("678")) #baştaki ve sondaki kısımları belirtilen şekilde kırpıyor
print("---------------")
print(dir(a)) 

#kullanılabilir metodlar str
'__add__'  
'__class__', 
'__contains__',
'__delattr__',
'__dir__',
'__doc__',
'__eq__', 
'__format__',
'__ge__',
'__getattribute__',
'__getitem__', 
'__getnewargs__',
'__getstate__',
'__gt__',
'__hash__', 
'__init__',
'__init_subclass__',
'__iter__',
'__le__', 
'__len__',
'__lt__',
'__mod__',
'__mul__',
'__ne__',
'__new__',
'__reduce__',
'__reduce_ex__',
'__repr__',
'__rmod__', 
'__rmul__', 
'__setattr__',
'__sizeof__',
'__str__', 
'__subclasshook__', 
'capitalize',
'casefold',
'center',
'count',
'encode', 
'endswith',
'expandtabs',
'find',
'format',
'format_map',
'index', 
'isalnum', 
'isalpha',
'isascii',
'isdecimal',
'isdigit',
'isidentifier',
'islower',
'isnumeric',
'isprintable',
'isspace',
'istitle',
'isupper',
'join',
'ljust',
'lower',
'lstrip',
'maketrans', 
'partition', 
'removeprefix', 
'removesuffix',
'replace',
'rfind',
'rindex', 
'rjust',
'rpartition',
'rsplit', 
'rstrip', 
'split', 
'splitlines', 
'startswith', 
'strip', 
'swapcase',
'title',
'translate',
'upper',
'zfill'

print(a.capitalize()) #en baştaki kelimenin baş harfi büyük
print(a.title()) #Her kelimenin baş harfi büyük
print("------------------------")

# print(a[20]) string index out of range -hata kodu-
print(a[3])
print(a[0:3])
print(a[3:7])
print("-------------------------------")


#TİP DÖNÜŞÜMLERİ

sayi1=int(input("ilk sayıyı giriniz"))
sayi2=float(input("ikinci sayiyi giririniz"))

toplam=sayi1+sayi2
print(toplam)


sayi1=str(input("ilk sayıyı giriniz"))
sayi2=str(input("ikinci sayiyi giririniz"))

toplam=sayi1+sayi2
print(toplam)

print("Feyza", "Nur", "Gökçe", sep="_") #fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belirteçlere argüman denir.


#VERİ YAPILARI

#listeler

# [], list()

notlar= [90,34,5,6,2]

print(notlar)
print(type(notlar))

liste=["a",3,5.34]
print(liste)

listegenis=["a",3,5.34,notlar]
print(listegenis)

print(type(listegenis[2]))

tum_liste=[liste,listegenis]
print(tum_liste)

aliste=[10,20,30,40,50]

print(aliste[0])
print(aliste[:2])
print(aliste[2:])

newlist=["a",10,[20,30,40,50]]
#print(newlist[3]) #3 elemanlıdır ve 0 1 2 indexten oluşur
print(newlist[2][1]) #30 sayısına erişmek için

bliste=["ali","veli","berkan","ayse"]

bliste[1]="veli_babasi"
print(bliste)

bliste[1]="veli"

bliste[:3]="alinin_babasi","velinin_babasi","berkanın_babasi"
print(bliste)

bliste=["ali","veli","berkan","ayse"]
bliste=bliste+["kemal"] #kalici halde kemal i listeye ekledik
print(bliste)

del bliste[2]
print(bliste)


cliste=["feyza","sude","furkan"]

cliste.append("berkecan") #listeye ekledik

cliste.remove("berkecan") #listeden kaldırdık

cliste.insert(0,"gökçe") #indexe göre eleman ekleme
#cliste[0]="gökçe"#feyzanın yerini gökçe alıyor yani eklemiyor

print(cliste)

#her seferinde listenin sonuna eleman eklemk için ;

cliste.insert(len(cliste),"beren")

print(cliste)

cliste.pop(0) #silmek
print(cliste)


dliste=["ali","veli","isik","ali","veli"]

dliste_yedek=dliste.copy() #listenin ilk halini korumak için kopyalama

print(dliste.count("ali"))

dliste.extend(["a","b",10]) #iki listeyi birleştirme

print(dliste)

dliste.index("ali")

dliste.reverse() #terine cevirme
print(dliste)

fliste=[1,3,4,5,76,87,3]
fliste.sort()
print(fliste)

fliste.clear()
print(fliste)

#listeler kapsayıcıdır sıralıdır değiştirilebilir

#DEMETLER(TUPLE)
#değiştirilemezler
#kapsayıcı
#sıralıdır

t=("ali","veli",1,2,3.2,[1,2,3,4])
#iki şekildede tuple uluşturulabiliyor
t="ali","veli",1,2,3.2[1,2,3,4]

t=("eleman") 
print(type(t)) #sonuş str olacaktır tuple olması için tek elemanlılarda
t=("eleman",) #bunu yaz

t="ali","veli",1,2,3.2,[1,2,3,4]
t[1]
t[0:3]
t[2]


#SÖZLÜKLER
#Sırasız
#Kapsayıcı
#değiştirilebilir

sozluk= {"red":["kirmizi",20],
        "blue":"mavi",
        "yellow":"sari"}
#key,ne olduğu
print(sozluk)
print(len(sozluk)) #key 'e göre

#sozluk[0] key eror hatası bunun sebebi sozlukların sırasız olması ve elemanlara index mantığı ile ulaşamadığımız.

print(sozluk["blue"]) #bu şekilde çağrılabilir
'''



