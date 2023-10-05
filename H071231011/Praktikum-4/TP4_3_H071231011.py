def maksimum_angka (angka):
    angka_terbesar = angka[0]

    for i in angka:
        if i > angka_terbesar:
            angka_terbesar = i

    return angka_terbesar

#case1
daftarAngka = [20, 12, 3, 4, 11, 5, 7, 8, 9, 16]
print(">>", maksimum_angka(daftarAngka))

