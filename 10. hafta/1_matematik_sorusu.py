"""
1. Denklem i cevaplayın
"""
n = eval(input("n değerini giriniz : "))

toplam = 0

for k in range(1, n+1):
    toplam += (k + 5 * k) / n

toplam += 2
print("A :", toplam)

