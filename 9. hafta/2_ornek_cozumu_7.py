'''
    7- By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
        What is the 10001st prime number?
        10001 inci asal sayı kaçtır?
'''
import math
sayac = 1
for i in range(3, 1000000, 2):
    asal_mi = True
    for s in range(3, round(math.sqrt(i))+1):
        if i % s == 0:
            asal_mi = False
            break
    if asal_mi:
        sayac += 1
        if sayac == 10001:
            print(i)
