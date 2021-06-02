# 1- 1 den 100 e kadar olan asal sayıları bulup ekrana yazdıran program

for i in range(3, 100):
    asal_mi = True
    for s in range(2, i):
        if i % s == 0:
            asal_mi = False
            break
    if asal_mi:
        print(i)
