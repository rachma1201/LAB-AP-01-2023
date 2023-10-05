def kucing_tikus(kucingA,kucingB,tikus):
    jarak_A = ((tikus - kucingA)**2)**0.5
    jarak_B = ((tikus - kucingB)**2)**0.5

    if jarak_A > jarak_B:
        print("Cat B")
    elif jarak_B > jarak_A:
        print("Cat A")
    else:
        print("Mouse C")

kucing_tikus(kucingA = 30,kucingB = 18,tikus = 16)