input_angka = input("Masukkan angka : ").split()

genap = []
ganjil = []
habis_dibagi = []

for angka_str in input_angka:
    angka = int(angka_str)
    if angka %2 == 0:
        genap.append(angka)
    elif angka %2 == 1:
        ganjil.append(angka)
    if angka %5 == 0:
        habis_dibagi.append(angka)

print("Angka Genap:", genap)
print("Angka Ganjil:", ganjil)
print("Angka yang Habis Dibagi 5:", habis_dibagi)
