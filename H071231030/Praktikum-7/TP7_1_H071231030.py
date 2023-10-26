import os
import datetime
import random

def GGG():
    print('='*70)

def createHistory():
    with open("trx_history", 'w') as file:
        file.write(f"{'='*70}\n")
        file.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        file.write(f"{'='*70}\n")
        file.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':^24}|\n")
        file.write(f"{'='*70}\n")

def addHistory(waktu, id, nominal):
    with open("trx_history",'a') as file:
        file.write(f"|{waktu:^18}|{id:<24}|{'Rp' + str(nominal):^24}|\n")
        file.write(f"{'-'*70}\n")

def struk():
    #isi struk
    global kasir, WAKTU, tampung, total_belanja, file_path
    with open(file_path, "w") as data:
        data.write(f"{'TOKO JAYA ABADI':^70}\n\n")
        data.write(f"{'='*70}\n")
        data.write(f"Nama kasir \t\t: {kasir}\n")
        data.write(f"Waktu transaksi \t: {WAKTU}\n")
        data.write(f"{'='*70}\n\n")
        data.write(f"{'Daftar Produk':^70}\n\n")
        data.write(f"{60*'=':^70}\n")
        data.write(f"{5*' '}|{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^15}|\n")
        data.write(f"{60*'=':^70}\n")
        for item in daftar_item:
            if len(item["nama"]) > 20:
                item["nama"] = item["nama"][:17] + "..."
            data.write(f"{5*' '}|{item['nama']:<20}|{'Rp' + str(item['harga']):>12}|{item['jumlah']:^8}|{'Rp' + str(item['total barang']):>15}|\n")
        data.write(f"{60*'=':^70}\n")
        data.write(f"{' '*5}|{'TOTAL':^42}|{'Rp' + str(total_belanja):>15}|\n")
        data.write(f"{60*'=':^70}\n\n")
        data.write(f"{'='*70}\n")
        data.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
        data.write(f"{'='*70}\n")

def id(kasir):
    inisial = ""
    x = list(kasir.split())
    for i in x: inisial += i[0]
    waktu = datetime.datetime.now()
    kode = str(random.randint(100,999))
    file_name = inisial + waktu.strftime("%y%m%d%H%M") + kode 
    return file_name

folder_path = "Invoices"
daftar_item = []

GGG()
print('SELAMAT DATANG'.center(70))
GGG()
kasir = input("Masukkan nama Kasir\t: ").title()

while True:
    GGG()
    print('Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar')
    GGG()
    opsi = int(input("Masukkkan opsi pilihan\t: "))
    GGG()
    match opsi:
        case 1:
            ID = id(kasir)
            file_name = ID + ".txt"
            file_path = os.path.join(folder_path, file_name)
            
            waktu = datetime.datetime.now()
            WAKTU = waktu.strftime("%y/%m/%d %H:%M")
            total_belanja = 0      

            while True:
                nama = input("Masukkan nama produk\t: ")
                harga = int(input("Masukkan harga produk\t: "))
                jumlah = int(input("Masukkan jumlah produk\t: "))
                total_barang = harga*jumlah
                total_belanja += total_barang
                GGG()

                item = {
                    "nama" : nama,
                    "harga" : harga,
                    "jumlah" : jumlah,
                    "total barang" : total_barang,
                }
                daftar_item.append(item)
                
                isTambah = input("Tambah produk? (y/t)\t: ")
                if isTambah == 't':
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                    if not os.path.exists("trx_history"):
                        createHistory()
                    struk()

                    daftar_item.clear()
                    GGG()
                    print(f"{'TRANSAKSI BERHASIL':^70}")
                    break
                GGG()
            # riwayat transaksi
            addHistory(WAKTU, ID, total_belanja)

        case 2:
            cari = input("Masukkan ID file transaksi : ")
            cari_path = folder_path + "/" + cari + ".txt"
            if os.path.exists(cari_path):
                with open(cari_path, "r") as file:
                    GGG()
                    print(f"\n\n{file.read()}")
            else:
                print(f"File dengan ID {cari} tidak ditemukan")

        case 3:
            print(f"SELAMAT TINGGAL {kasir.upper()}".center(70))
            GGG()
            break
        
        case _:
            print("INPUT TIDAK VALID".center(70))