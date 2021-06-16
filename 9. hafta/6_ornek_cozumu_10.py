"""
10- İki dik kenarı girilen dik üçgenin hipotenüsünü hesaplayan algoritma
"""
import math
dik_kenar_1 = eval(input("1. Dik Kenarı Giriniz : "))
dik_kenar_2 = eval(input("2. Dik Kenarı Giriniz : "))

kareleri_toplami = dik_kenar_1 ** 2 + dik_kenar_2 ** 2
print("Kareleri Toplamı :", kareleri_toplami)

print("Hipotenüs uzunluğu :", math.sqrt(kareleri_toplami))



