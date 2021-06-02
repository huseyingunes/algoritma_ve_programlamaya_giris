'''
2- 100 den 1000 e kadar olan palindromik sayıları ekrana yazdıran program
    Palindromik sayı, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılara verilen isimdir.
    Örn: 101
'''

for i in range(100, 1001):
    sayi = str(i)
    # print(sayi[0], "-", sayi[1], "-", sayi[2])
    if sayi[0] == sayi[2]:
        print(i)
