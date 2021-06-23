"""
x = (3 üzeri c bölü karekök 81) + Karekök içinde a nın karesi + b nin karesi

Denkleminde x değerini a, b ve c değerlerini kullanıcıdan alarak
hesaplayan programı yazınız.
"""
import math

a = eval(input("a : "))
b = eval(input("b : "))
c = eval(input("c : "))

x = math.pow(3, c) / math.sqrt(81)
x += math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print("X :", x)
