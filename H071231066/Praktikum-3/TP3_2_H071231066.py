hargabarang = int(input("Masukkan Harga Barang : "))
uang = int(input("Masukkan Berapa uang anda : ")) 
kembalian = uang - hargabarang
if kembalian < 0: #Logika nya jika uang kita kurang saat berbelanja maka kasir akan bilang uang tidak cukup
    print("Uang anda kurang!")
else: 
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000] #ini pecahan memakai kurung siku karena list
    for i in pecahan:
        jumlah = kembalian // i
        kembalian = kembalian - jumlah * i
        print(f"{jumlah} Jumlah uang bernilai Rp.{i}")