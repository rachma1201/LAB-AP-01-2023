simpan = {}
print("Selamat datang untuk memulai silahkan input data anda")

simpan['nama'] = input("input nama : ")
simpan['umur'] = input("input umur: ")
simpan['alamat'] = input("input alamat : ")

while True:
    print("="*50)
    print(f"Selamat datang {simpan['nama']} silahkan pilih opsi")
    print("1. Detail anda")
    print("2. Ubah nama")
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. Keluar")
    print("="*50)

    opsi = input("input opsi : ")
    print("="*50)

    if opsi == "1":
        print(f"Data anda adalah \nNama: {simpan['nama']}\nUmur:{simpan['umur']}\nAlamat:{simpan['alamat']}")
    elif opsi == "2":
        nama = input("silahkan input nama baru : ")
        simpan["nama"] = nama
        print("Data anda sukses diperbarui")
    elif opsi == "3":
        umur = input("silahkan input umur baru : ")
        simpan["umur"] = umur
        print("Data anda sukses diperbarui")
    elif opsi == "4":
        alamat = input("silahkan input alamat baru : ")
        simpan["alamat"] = alamat
        print("Data anda sukses diperbarui")
    elif opsi == "5":
        print(f"Selamat tinggal {simpan['nama']}")
        break
    else:
        print("Opsi tidak valid. Silahkan pilih opsi yang valid ")