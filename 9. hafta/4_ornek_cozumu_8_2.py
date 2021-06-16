"""
8- Rastgele oluışturulan 10 tane sayıyı bir listeye atınız ve listeyi kendi yazdığınız algoritma ile
küçükten büyüğe sıralayınız.
"""
import random
liste = []
for i in range(0, 10):
    liste.append(random.randint(0, 100))

print(liste)

for i in range(0, 10):
    for s in range(0, 9):
        if liste[s] > liste[s+1]:
            liste[s], liste[s+1] = liste[s+1], liste[s]

print(liste)
