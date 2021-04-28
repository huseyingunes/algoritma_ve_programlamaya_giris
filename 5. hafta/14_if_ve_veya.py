'''
Kullanıcıdan kilosunu ve boyunu girmesini isteyin.
Kilosu 50-60 aralğındaysa ve
    boyu 160-170 aralığındaysa "ideal kişi" yazsın.
'''

kilo = eval(input("Kilonuzu Giriniz : "))
boy = eval(input("Boyunuz Giriniz : "))

if kilo >= 50 and kilo <=60 and boy >= 160 and boy <= 170:
    print("ideal kişi")
else:
    print("ideal kişi siz değilsiniz")
