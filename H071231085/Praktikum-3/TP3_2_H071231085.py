harga_barang = int(input())
uang = int(input())

kembalian = uang - harga_barang
if kembalian < 0:
    print("uang kurang!")
else:
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    for x in pecahan:
        jumlah = kembalian // x
        kembalian = kembalian % x
        print(f"{jumlah} uang sejumlah Rp.{x}")