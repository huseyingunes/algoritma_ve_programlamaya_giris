"""
2. Denklem i cevaplayın
"""
n = eval(input("n değerini giriniz : "))

carpim = 1

for k in range(1, n+1):
    carpim *= (k - n) / (k + n)
    print(k, ":", carpim)

carpim *= 3

print("A :", carpim)
