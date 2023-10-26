import os
import time
import random

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
        file_invoice.write(f"\n {f'TOKO {nama_kasir.upper()}':^66}\n")
        file_invoice.write("=" * 66 + "\n")
        file_invoice.write(f"{'Kasir':<20} : {nama_kasir}\n".title())
        file_invoice.write(f"{'Waktu transaksi':<20} : " + (time.strftime("%d/%m/%Y %H:%M", time.localtime()) + "\n"))
        file_invoice.write("=" * 66 + "\n")
        file_invoice.write(f"\n{'Daftar Produk':^66}\n")
        file_invoice.write(f"""
    {'=' * 58}
    |{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^13}|
    {'=' * 58}""") # Format head table Daftar Produk
        for i in produk:
            nama, harga, jumlah = i
            if len(nama) > 15:
                nama = nama[:15] + "..."
            file_invoice.write(f"\n    | {nama:<18} |" + f" Rp.{harga:>7} |" + f" {jumlah:^6} " + f"| Rp.{harga * jumlah :>8} |")
        file_invoice.write('\n' + f"{'=' * 58}".center(66))
        file_invoice.write('\n' + f'    |       TOTAL                              | Rp.{total:>8} |' + '\n')
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
    ID = id_transaksi.replace('.txt','')
    if os.path.exists(riwayat_file) == False: # Cek apakah file sudah ada
                    # Membuat tabel riwayat transaksi jika file belum ada
            with open(riwayat_file, 'w') as history:
                history.write(f"""
{'=' * 80}
|{'RIWAYAT TRANSAKSI':^78}|
{'=' * 80}
| {'Waktu':^20} | {'ID':^20} | {'Nominal':^30} |
{'=' * 80}
""") 
                history.write(f"""
| {waktu_transaksi:^20} | {ID:^20} | RP.{total:>27} |
{'=' * 80}""")
    else: # Membuat tabel riwayat transaksi jika file sdh ada
            with open(riwayat_file, 'a') as history:
                history.write(f"""
| {waktu_transaksi:^20} | {ID:^20} | Rp.{total:>27} |
{'=' * 80}""") # Format tabel riwayat transaksi jika file sudah ada
                
# Fungsi untuk membuat folder "invoices" jika belum ada


print("=" * 70)
print(f"{'SELAMAT DATANG':^70}")
print("=" * 70)
nama_kasir = input("Masukkan nama kasir: ")
print("=" * 70)
jumlah = len(nama_kasir)
inisial = (nama_kasir[0] + nama_kasir[jumlah//2] + nama_kasir[-1]).upper()

while True:
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("=" * 70)
    opsi = input("Masukkan opsi pilihan: ")
    if opsi == "1":
        id_transaksi = f'{Id_Transaksi()}.txt'
        produk = []
        total = 0
        while True:
            print(f"{'=' * 70}")
            nama_produk = input("Masukkan nama produk : ")
            harga_produk = int(input("Masukkan harga produk : "))
            jumlah_produk = int(input("Masukkan jumlah produk : "))
            produk.append((nama_produk, harga_produk, jumlah_produk))
            total += harga_produk * jumlah_produk
            print("="*70)
            tambah_produk = input("Tambahkan produk (y/t) : ").lower()
            if tambah_produk != "y":
                break
        cetak_invoice(id_transaksi, nama_kasir, produk, total)
        riwayat_transaksi(id_transaksi, total)
        print(f"{'=' * 70 }\n" + f"{'TRANSAKSI BERHASIL':^70}" + f"\n{'=' * 70 }")
    elif opsi == "2":
        id_transaksi1 = input("Masukkan ID transaksi: ")
        mencari(id_transaksi1)
    elif opsi == "3":
        print("="*70)
        print(f"{'SAMPAI JUMPA':^70}")
        print("="*70)
        break
        
    else:
        print("Opsi tidak valid")
    