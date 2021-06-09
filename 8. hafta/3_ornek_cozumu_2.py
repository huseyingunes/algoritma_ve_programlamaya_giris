'''
    2- 1 den 1.000.000 a kadar olan asal sayıları bulup ekrana yazdıran program
'''
import math
import time
baslangic_saati = time.time()
for i in range(3, 1000000, 2):
    asal_mi = True
    for s in range(3, round(math.sqrt(i))):
        if i % s == 0:
            asal_mi = False
            break
    if asal_mi:
        print(i)

print("Geçen Süre :", (time.time() - baslangic_saati))
