import math

# a = eval(input("a : "))
# a değerini kullanıcıdan almasakta olurmuş

b = eval(input("b : "))
c = eval(input("c : "))

toplam = 0
for a in range(c, b+1):
    toplam += math.sqrt(a+b) / math.pow(a, b)

h = math.pow(toplam, 1/3)
print("h :", h)

