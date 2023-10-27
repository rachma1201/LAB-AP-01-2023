print("MEMBUAT KASIR KEMBALIAN")

a = int(input("Masukkan nilai total belanja: Rp."))
b = int(input("Masukkan uang yang dibayar: Rp. "))
c = b - a
print(f"Kembaliannya sebesar Rp. {c} dengan Rincian kembalian")
d = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for x in d:
    y = c//x
    z = c% x
    
    # while c >= d[x]:
    #     c = c - d[x]
    #     i = i + 1
    # if (i > 0):
    print(f"Uang Rp. {y} sebanyak {x} lembar")
