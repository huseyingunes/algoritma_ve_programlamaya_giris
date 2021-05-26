'''
Kullanıcının 0-100 aralığında aklından tuttuğu sayıyı
deneme yapılma yöntemi ile tahmin ederek bulan programı yazınız.
Kullanıcı her tahminden sonra bilgisayara aşağı (a), yukarı (y) ya da doğru (d)
diye bilgisayarı yönlendirmelidir.
3 tane yapı kullanılmalı
1- rastgele sayı üretme
2- koşullu ifadeler
3- while döngüsü
'''
from random import *
en_kucuk = 0
en_buyuk = 100
while True:
    sayi = randint(en_kucuk, en_buyuk)
    print("Aklından tuttuğun sayı :", sayi)
    cevap = input("Doğru mu? : ")
    if cevap == "d":
        print("Sayını doğru tahmin ettim program bitti...")
        break  # döngüyü sonlandırır
    elif cevap == "a":
        en_buyuk = sayi - 1
    elif cevap == "y":
        en_kucuk = sayi + 1

print("SON")



