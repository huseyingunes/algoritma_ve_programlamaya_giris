'''
Kullanıcının yaşını sorun
Yaşı 10 dan küçükse çocuk
10-20 aralığındaysa ergen
20-30 aralığındaysa genç
30-40 aralığındaysa olgun
40 tan büyükse elveda
yazsın.
'''
yas = eval(input("Yaşınızı Giriniz : "))

if yas < 10:
    print("Sen daha çocuksun")
elif yas < 20:
    print("Sen ergensin")
elif yas < 30:
    print("Gençsin")
elif yas < 40:
    print("Olgunsun")
else:
    print("Elveda")


print(yas)
