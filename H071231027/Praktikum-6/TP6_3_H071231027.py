bilangan = list(map(int,input("\nMasukkan beberapa angka: ").split()))
genap, ganjil, habisdibagi5 = [], [], []
for i in bilangan:
    if i%2 == 0:
        genap.append(i)
    elif i%2 != 0:
        ganjil.append(i)
    if i%5 == 0:
        habisdibagi5.append(i)
print(f'Angka Genap: {genap}\nAngka Ganjil: {ganjil}\nAngka yang habis dibagi 5: {habisdibagi5}\n')

