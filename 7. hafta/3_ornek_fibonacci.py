'''
3- 1 ve 1 değerlerinden başlayarak 1000 e kadar olan fibonacci dizisi elemanlarını ekrana yazdıran programı yazınız.
    Fibonacci dizisi, her sayının kendinden öncekiyle toplanması sonucu oluşan bir sayı dizisidir.
    Yani 1+1 = 2
    2+1 = 3
    3+2 = 5
    5+3 = 8 ...
    1, 1, 2, 3, 5, 8, 13, 21, 34, ...
'''

sayi1 = 1
sayi2 = 1
print(sayi1)
print(sayi2)
while True:
    sayi1_eski_degeri = sayi1
    sayi1 = sayi2
    sayi2 = sayi1_eski_degeri + sayi2
    if sayi2 > 1000:
        break
    print(sayi2)

