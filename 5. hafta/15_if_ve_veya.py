'''
Kullanıcıdan kilosunu ve boyunu girmesini isteyin.
Kilosu 50-60 aralğındaysa
    VEYA
boyu 160-170 aralığındaysa "ideal kişi" yazsın.
'''

kilo = eval(input("Kilonuzu Giriniz : "))
boy = eval(input("Boyunuz Giriniz : "))


if 50 <= kilo <= 60 or 160 <= boy <= 170:
    print("ideal kişi")
else:
    print("ideal kişi siz değilsiniz")
