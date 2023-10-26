import os #Membuat dan mencari file
import time #Memanggil waktu
import random #Memanggil angka acak

# Fungsi untuk membuat folder "invoices" jika belum ada
if not os.path.exists("invoices"):
    os.mkdir("invoices")

# Fungsi untuk membuat ID transaksi
def Id_Transaksi():
    waktu = time.strftime("%y%m%d%H%M", time.localtime())
    id_transaksi = f'{inisial}{waktu}{random.randint(100, 999)}'
    return id_transaksi

# Fungsi untuk mencetak invoice
def cetak_invoice(id_transaksi, nama_kasir, produk, total):
    nama_file = f"invoices/{id_transaksi}"
    with open(nama_file, "w") as file_invoice:
        file_invoice.write(f"TOKO {nama_kasir}".center(66).upper() + "\n")
        file_invoice.write("=" * 66 + "\n")
        file_invoice.write(f"{'Kasir':<20}: {nama_kasir}\n".title())
        file_invoice.write(f"{'Waktu transaksi':<20}: " + (time.strftime("%d/%m/%Y %H:%M", time.localtime()) + "\n"))
        file_invoice.write("=" * 66 + "\n")
        file_invoice.write("\n" + "Daftar Produk".center(66) + "\n")
        file_invoice.write(f"""
    {'=' * 58}
    |        Nama        |    Harga   | Jumlah |    Total    |
    {'=' * 58}""") # Format head table Daftar Produk
        for i in produk:
            nama, harga, jumlah = i
            if len(nama) > 15:
                nama = nama[:15] + "..."
            file_invoice.write(f"\n    | {nama:<18} |" + f"Rp.{harga:>8} |" + f" {jumlah:^6} " + f"|Rp.{harga * jumlah :>9} |")
        file_invoice.write('\n' + f"{'=' * 58}".center(66))
        file_invoice.write('\n' + f'    |       TOTAL                              |Rp.{total:>9} |' + '\n')
        file_invoice.write(f"{'=' * 58}".center(66) + f"\n\n{'=' * 66}\n" + 'TERIMA KASIH TELAH BERBELANJA'.center(66) + f"\n{'=' * 66}")


# Fungsi untuk mencari invoice berdasarkan ID
def mencari(id_transaksi):
    nama_file = f"invoices/{id_transaksi}.txt"
    if os.path.exists(nama_file):
        print(f"{'_' * 66}")
        with open(nama_file, 'r') as file_invoice:
            print(file_invoice.read())
        print(f"{'_' * 66}")
    else:
        print("Invoice tidak ditemukan")

# Fungsi untuk mencatat transaksi ke dalam riwayat transaksi
def riwayat_transaksi(id_transaksi, total):
    riwayat_file = "trx_history.txt"
    waktu_transaksi = time.strftime("%d/%m/%Y %H:%M", time.localtime())
    if not os.path.exists(riwayat_file): # Cek apakah file sudah ada
                    # Membuat tabel riwayat transaksi jika file belum ada
            with open(riwayat_file, 'a') as history:
                history.write(f"""
{'=' * 80}
|                              RIWAYAT TRANSAKSI                               |
{'=' * 80}
| {'Waktu':^20} | {'ID':^20} | {'Nominal':^30} |
{'=' * 80}
""") 
                history.write(f"""
| {waktu_transaksi:^20} | {id_transaksi:^20} | {total:>30} |
{'=' * 80}""")
                
    else: # Membuat tabel riwayat transaksi jika file sdh ada
            with open(riwayat_file, 'a') as history:
                history.write(f"""
| {waktu_transaksi:^20} | {id_transaksi:^20} | {total:>30} |
{'=' * 80}""") # Format tabel riwayat transaksi jika file sudah ada
                


print("=" * 50)
print("Selamat datang".center(50))
print("=" * 50)
nama_kasir = input("Masukkan nama kasir : ")
print(f"{'=' * 50}")
jumlah = len(nama_kasir)
inisial = (nama_kasir[0] + nama_kasir[jumlah//2] + nama_kasir[-1]).upper()
    
while True:
    print("Pilih opsi\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar")
    print("=" * 50)
    option = input("Masukkan opsi pilihan : ")

    if option == "1":
            
        id_transaksi = f'{Id_Transaksi()}.txt'
        produk = []
        total = 0
        while True:
            print(f"{'=' * 50}")
            nama_produk = input("Masukkan nama produk : ")
            harga_produk = int(input("Masukkan harga produk : "))
            if harga_produk < 500:
                print("Harga Produk Invalid")
                continue
            jumlah_produk = int(input("Masukkan jumlah produk : "))
            produk.append((nama_produk, harga_produk, jumlah_produk))
            total += harga_produk * jumlah_produk
            tambah_produk = input("=" * 50 +"\nTambahkan produk (y/t) : ").lower()
            if tambah_produk == "t":
                break
        cetak_invoice(id_transaksi, nama_kasir, produk, total)
        riwayat_transaksi(Id_Transaksi(), total)
        print(f"{'=' * 50 }\n" + 'TRANSAKSI BERHASIL'.center(50) + f"\n{'=' * 50 }")

    elif option == "2":
        print(f"{'=' * 50}")
        id_transaksi = input("Masukkan ID transaksi: ")
        mencari(id_transaksi)
    elif option == "3":
        print(f"{'='*50}\n" + 'SAMPAI JUMPA'.center(50) + f"\n{'='*50}")
        break
    else:
        print("Opsi tidak valid")