print ("\nSelamat Datang untuk memulai silahkan input data anda")
data = {}
data["Input Nama"] = input("Input Nama   : ")
data["Input Umur"] = input("Input Umur   : ")
data["Input Alamat"] = input("Input Alamat : ")

while True:
    print()
    print('='*50, end='')
    print(f"\nSelamat Datang {data['Input Nama']} silahkan pilih opsi")
    print('='*50, end='')
    
    print(f"\n1. Detail anda \n2. Ubah Nama \n3. Ubah Umur \n4. Ubah Alamat \n5. Keluar")
    print('='*50, end='')
    pilih = input("\nInput Opsi : ")    
    print('='*50, end='')

    if pilih == "1":
        print("\nData anda adalah")
        print(f"Nama   : {data['Input Nama']}\nUmur   : {data['Input Umur']}\nAlamat : {data['Input Alamat']}")
    
    elif pilih == "2":
        data['Input Nama'] = input("\nSilahkan Input Nama baru : ")
        print("Data anda berhasil diperbarui")
    elif pilih == "3":
        data['Input Umur'] = input("\nSilahkan Input Umur baru : ")
        print("Data anda berhasil diperbarui")
    elif pilih == "4":
        data['Input Alamat'] = input("\nSilahkan Input Alamat baru : ")
        print("Data anda berhasil diperbarui")
    elif pilih == "5":
        print(f"\nSelamat Tinggal {data['Input Nama']}\n")
        break
    else:
        print("\nOpsi Tidak Ada")