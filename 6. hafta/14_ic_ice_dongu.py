'''
Çarpım tablosunu ekrana yazdırınız
'''

for i in range (1, 11):
    print(i, "sayısının çarpım tablosu :")
    for s in range(1, 11):
        print(i, "*", s, "=", (i*s))
