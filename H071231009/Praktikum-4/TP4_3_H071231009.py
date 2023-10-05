def angka_terbesar(*maksimum):
    terbesar = int(maksimum[0])
    for i in maksimum:
        if int(i) > terbesar:
            terbesar = int(i)
    
    return terbesar

ang = input("Masukkan angka dipisahkan spasi: ").split()
hasil = angka_terbesar(*ang)
print(hasil)