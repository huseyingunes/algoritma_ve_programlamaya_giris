'''
Bilgisayarın 0-100 aralığında aklından tuttuğu sayıyı
deneme yapılma yöntemi ile tahmin ederek kullanıcının bulduğu programı yazınız.
Kullanıcının her tahmininden sonra bilgisayara aşağı (a), yukarı (y) ya da doğru (d)
diye kullanıcıyı yönlendirmelidir.
'''
from random import *
sayi = randint(0, 100)

while True:
    cevap = int(input("Aklından tuttuğun sayı : "))
    if cevap == sayi:
        print("Doğru tahmin. Tabrikler...")
        break
    elif cevap < sayi:
        print("Yukarı")
    else:
        print("Aşağı")

print("SON")

