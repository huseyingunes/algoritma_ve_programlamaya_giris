'''
Kullanıcıdan 5 tane sayı girmesini isteyiniz
Bu sayıları bir listeye kaydediniz
Daha sonra bu sayıların tek olanlarını ekrana yazdırınız
'''

sayilar = []
for i in range(1, 6):
    sayi = eval(input(str(i)+". sayı : "))
    sayilar.append(sayi)

for sayi in sayilar:
    if sayi % 2 == 1:
        continue
    print(sayi)
