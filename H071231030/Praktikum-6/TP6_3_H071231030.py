pembagian = input("Masukkan Angka : ")
bilangan = pembagian.split()

genap = []
ganjil = []
habis5 = []
for i in bilangan:
    i = int(i)
    if i%2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)
    if i%5 == 0:
        habis5.append(i)

print(f"Angka Genap : {genap}")
print(f"Angka Ganjil : {ganjil}")
print(f"Angka Yang Habis Dibagi 5 : {habis5}")