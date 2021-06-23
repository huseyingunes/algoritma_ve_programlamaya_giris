"""
x = (3 üzeri 5 bölü karekök 81) + Karekök içinde 3 ün karesi + 4 ün karesi
"""
import math

x = math.pow(3, 5) / math.sqrt(81)
x += math.sqrt(math.pow(3, 2) + math.pow(4, 2))

print("X :", x)
