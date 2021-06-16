"""
9- 1’den 1000’e kadar olan çift tamsayıların toplamını hesaplayan algoritma
"""
toplam = 0
for i in range(1, 1000):
    if i % 2 == 0:
        print("Toplam :", toplam, "+", i, "=", toplam+i)
        toplam += i

print("Toplam :", toplam)
