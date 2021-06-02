def sayi_tek_mi(sayi):
    if sayi % 2 == 1:
        return True
    else:
        return False

if sayi_tek_mi(16):
    print("Bu sayı tekmiş")
else:
    print("Bu sayı çiftmiş")
