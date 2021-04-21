# 2- Finali ve ortalamasını alarak vize notunu hesaplayın
final = eval(input("Final notunuz :"))
ortalama = eval(input("Ortalama notunuz :"))

ara_deger = final * 0.6
ara_deger_2 = ortalama-ara_deger
vize = (ara_deger_2*10)/4

print("Vize notunuz :", int(vize))

print("Vize notunuz :", int((ortalama-(final * 0.6))*10/4))
