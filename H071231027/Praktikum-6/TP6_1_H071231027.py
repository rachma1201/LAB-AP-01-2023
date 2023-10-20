print("\nSelamat datang untuk memulai silahkan input data anda")
data = {}
data["Input nama"] = input("Input nama : ").title()
data["Input umur"] = input("Input umur : ")
data["Input alamat"] = input("Input alamat : ").capitalize()
while True:
    print()
    panjang = len(f'Selamat datang {data["Input nama"]} silahkan pilih opsi')
    print('='*panjang)
    print(f'Selamat datang {data["Input nama"]} silahkan pilih opsi')
    print('='*panjang)
    print(f'1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar')
    print('='*panjang)
    pilih = input("Input opsi: ")
    print('='*panjang)

    if pilih == '1':
        print("Data anda adalah")
        print(f'Nama: {data["Input nama"]}\nUmur: {data["Input umur"]}\nAlamat: {data["Input alamat"]}')
    elif pilih == '2':
        data["Input nama"] = input("Silahkan input nama baru : ")
        print('Data anda sukses diperbarui')
    elif pilih == '3':
        data["Input umur"] = input("Silahkan input umur baru :")
        print('Data anda sukses diperbarui')
    elif pilih == '4':
        data["Input alamat"] = input("Silahkan input alamat baru :")
        print('Data anda sukses diperbarui')
    elif pilih == '5':
        print(f"\nSelamat Tinggal {data['Input nama']} :)\n")
        break
    else:
        print('Opsi Tidak ada')