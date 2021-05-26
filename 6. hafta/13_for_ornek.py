'''
Kullanıcıdan 5 tane sayı girmesini isteyiniz
Bu sayıları bir listeye kaydediniz
Daha sonra Bu sayıların toplamlarını ve çarpımlarını
en büyüğünü ve en küçüğünü ekrana yazdırınız
'''
sayilar = []
for i in range(1, 6):
    sayi = eval(input(str(i)+". sayı : "))
    sayilar.append(sayi)

print(sayilar)
toplam = 0
carpim = 1
en_buyuk = sayilar[0]
en_kucuk = sayilar[0]

for sayi in sayilar:
    toplam += sayi
    carpim *= sayi
    if en_buyuk < sayi:
        en_buyuk = sayi
    if en_kucuk > sayi:
        en_kucuk = sayi

print("Toplamları :", toplam)
print("Çarpımları :", carpim)
print("En Büyük :", en_buyuk)
print("En Küçük :", en_kucuk)

