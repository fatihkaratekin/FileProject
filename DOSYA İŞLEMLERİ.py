#dosya açma
#file = open("C:/Users/Fatih Karatekin/Desktop/bilgilerigöster.txt","w" ,encoding= "utf-8")
# w harfi write anlamında yazdırma işleminde kullanılır dosya 1 kere yazılır.
# a harfi ekleme yapmak için kullanılır dosya silinse bile üstüme ekleme yapar.
#Türkçe karakter istiyorsan encoding # utf-8 kullanılcak
#file.write("Fatih Karatekin enter the TXT...\n""ekleme yapıldı\n""2.ekleme yapıldı\n")
#file.close()

#dosya okuma işlemi için
file = open("C:/Users/Fatih Karatekin/Desktop/bilgilerigöster.txt","r", encoding="utf-8")
for i in file:
    print(i , end = "")

#file.read() okuma işleminde kullanılan bir başka okuma metodudur

file = open("C:/Users/Fatih Karatekin/Desktop/bilgilerigöster.txt","r", encoding="utf-8")

bilgi = file.read()
print("dosyanın getirildi:")
print(bilgi)

#readline() metodu dosyanın sadece ilk satırını alır birkaç kez  çalışırsa çalıştıgı kadar alır.

file = open("C:/Users/Fatih Karatekin/Desktop/bilgilerigöster.txt","r", encoding="utf-8")
print("İLK SATIR ALINDI")
print(file.readline())

#readlines() metodu liste şeklinde alır gösterir

file = open("C:/Users/Fatih Karatekin/Desktop/bilgilerigöster.txt","r", encoding="utf-8")
liste = file.readlines()
print("liste çagrıldı")
print(liste)