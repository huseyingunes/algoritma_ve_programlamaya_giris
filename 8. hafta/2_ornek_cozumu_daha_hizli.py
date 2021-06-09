'''
1- 1000 den 1000000 a kadar olan palindromik sayıları ekrana yazdıran program
    Palindromik sayı, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılara verilen isimdir.
    Örn: 101
'''

for i in range(1000, 1000000):
    metin_sayi = str(i)
    palindrom_mu = True
    for sayac in range(0, round(len(metin_sayi)/2)):
        if metin_sayi[sayac] != metin_sayi[-1-sayac]:
            palindrom_mu = False
            break
    if palindrom_mu:
        print(metin_sayi)

# 4 haneli örnek : 2002
# 5 haneli örnek : 15151, 50005
# 6 haneli örnek : 151151, 100001
