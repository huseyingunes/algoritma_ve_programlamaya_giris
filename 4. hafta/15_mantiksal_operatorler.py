'''
Mantıksal Operatörler
ve : and
veya : or
değil : not
'''

a = 5
b = 10
c = 20
d = 40
print("a b'den küçük ve c d'den küçük mü? : ", (a < b and c < d))

print("a b'den küçük ve c d'den büyük mü? : ", (a < b and c > d))

print("> : ", (a < b and c < d and a < c and b < d))

print("a b'den küçük veya c d'den küçük mü? : ", (a < b or c < d))

print("a b'den küçük veya c d'den büyük mü? : ", (a < b or c > d))

print("Normal : ", (a < b and c < d))
print("Değil : ", not(a < b and c < d))
print("Değil 2 : ", (a < b and not c > d))
