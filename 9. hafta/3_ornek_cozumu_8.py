"""
8- Rastgele oluışturulan 10 tane sayıyı bir listeye atınız ve listeyi kendi yazdığınız algoritma ile
küçükten büyüğe sıralayınız.
"""
import random
liste = []
for i in range(0, 10):
    liste.append(random.randint(0, 100))

sirali_liste = []
en_kucuk = 101
for s in range(0, 10):
    print(liste)
    for i in range(0, 10-s):
        if en_kucuk > liste[i]:
            en_kucuk = liste[i]
    print("Bulunan En Küçük :", en_kucuk)
    liste.remove(en_kucuk)
    sirali_liste.append(en_kucuk)
    en_kucuk = 101

print("Sıralı Liste :", sirali_liste)
print(liste)
