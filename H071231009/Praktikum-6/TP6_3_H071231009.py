x = list(map(int,input("Masukkan angka: ").split()))
a = []
b = []
c = []
for x in x:
    if x % 2 == 0:
        a.append(x)
    else:
        b.append(x)
    if x % 5 == 0:
        c.append(x)
print(f"Angka Genap: {a}")
print(f"Angka Ganjil: {b}")
print(f"Angka yang habis dibagi 5: {c}")