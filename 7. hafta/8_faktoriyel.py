'''
Kendisine parametre olarak gönderilen sayının faktöriyelini hesaplayarak
geri döndüren fonskiyonu ve
bir kullanım örneğini yazınız
'''

def faktoriyel(sayi):  # 5 sayısı için düşünelim
    carpinim = 1
    for i in range(2, sayi+1):
        carpinim *= i
    return carpinim

print("5 Faktöriyel :", faktoriyel(5))
print("10 Faktöriyel :", faktoriyel(10))
