"""
Öyle bir dizi düşünelim ki bu dizideki ilk üç elemandan sonraki elemanlar
kendisinden önce gelen üç elemanın çarpımı olsun.

Bu dizinin ilk 3 elemanı 1,2,3 olduğuna göre bundan sonraki 10 elemanı ekrana yazdıran programı yazınız.
"""
a, b, c = 1, 2, 3

for i in range(1, 11):
    hesap = a * b * c
    print(hesap)
    a, b, c = b, c, hesap
