"""
11- Girilen pozitif bir tamsayının tam bölenlerini bulup ekrana yazdıran algoritma
"""
sayi = eval(input("1 Sayı Giriniz : "))

for i in range(1, round(sayi/2)+1):
    if sayi % i == 0:
        print(i)
