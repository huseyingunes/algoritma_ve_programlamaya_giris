'''
    6- 13195 sayısının asal çarpanları 5,7,13 ve 29.
       O zaman 600851475143 sayısının en büyük asal çarpanı nedir?
'''
import math
import time

enbuyuk_asal = 1

def asal_mi(sayi):
    for s in range(3, round(math.sqrt(sayi))+1):
        if sayi % s == 0:
            return False
    return True

for i in range(3, round(math.sqrt(600851475143)), 2):
    if 600851475143 % i == 0:
        if asal_mi(i):
            print(i)
        if asal_mi(round(600851475143 / i)):
            print(round(600851475143 / i))


