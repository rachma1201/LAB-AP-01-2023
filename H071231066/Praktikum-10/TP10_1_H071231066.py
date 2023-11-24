import re
import os

class Detail:
    def __init__(self):
        self.nama = None
        self.email = None
        self.password = None
        
    def BuatNama(self, nama):
        self.nama = nama
    def BuatEmail(self, email):
        self.email = email
    def BuatPassword(self, password):
        self.password = password
        
def SelamatDatang():
    print(f"{'='*50}")
    print(f"Silahkan pilih opsi menu anda")
    print(f"1. Detail Anda\n2. Ubah Nama \n3. Jumlah Data Pada File\n4. Save Data Pada File\n5. Buat Data Baru\n6. Keluar")
    
def Nama():
    nama = input("Silahkan Masukkan Nama Anda : ")
    pattern_nama = re.fullmatch(r"[a-zA-Z0-9\s]*", nama)
    if pattern_nama:
        return nama
    else:
        print(f"{'='*50}\nFormat nama hanya berupa kombinasi huruf dan angka!\n{'='*50}")
        Nama()
        
def Email():
    email = input("Silahkan Masukkan Email Anda : ")
    pattern_email = re.fullmatch(r"[A-Za-z]*([0-9]{2,})?@[a-z]*\.([a-z]*\.)?(com|co\.id|ac\.id)$", email)
    if pattern_email:
        return email
    else:
        print(f"{'='*50}\nEmail yang anda masukkan salah!\n{'='*50}")
        Email()
    
def Password():
    password = input("Silahkan Masukkan Password Anda : ")
    pattern_password = re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{8,20}", password)
    if pattern_password:
        return password
    elif len(password) < 8 or len(password) > 20:
        print(f"{'='*50}\nPassword Harus Memiliki Panjang 8-20\n{'='*50}")
        Password()
    else:
        print(f"{'='*50}\nPassword yang anda masukkan terlalu lemah!\nGunakan minimal 1 huruf kapital, huruf kecil, dan angka\n{'='*50}")
        Password()

detail_akun = Detail()    
while True:
    SelamatDatang()
    pilihan = int(input("Silahkan Pilih Opsi Anda : "))
    match pilihan:
        case 1:
            if detail_akun.nama is None and detail_akun.email is None and detail_akun.password is None:
                print(f"{'='*50}\nData Saat Ini Kosong!")
            else:
                    print(f"{'='*50}\nData anda adalah :\nNama : {detail_akun.nama}\nEmail : {detail_akun.email}\nPassword : {detail_akun.password[0]}{(len(detail_akun.password)-2)*'*'}{detail_akun.password[-1]}")
        case 2:
            if detail_akun.nama is None:
                print(f"{'='*50}\nData Saat Ini Kosong!")
            else:
                detail_akun.BuatNama(input(f"{'='*50}\nSilahkan Input Nama Baru : "))
        case 3:
            print(f"{'='*50}")
            nama_file = input("Silahkan Masukkan Nama File : ") + ".txt"
            if not os.path.exists(nama_file):
                print(f"{'='*50}")
                print(f"Tidak Terdapat File Dengan Nama {nama_file[:-4]}")
                print("Jumlah data pada file berjumlah 0")
            else:
                with open(nama_file, mode="r") as cari_data:
                    pattern_jumlah = re.findall(r"Nama          : ", cari_data.read())
                    print(f"{'='*50}")
                    print("File Ditemukan")
                    print(f"Jumlah data pada file berjumlah {len(pattern_jumlah)}")
                     
                
        case 4:
            if detail_akun.nama is None and detail_akun.email is None and detail_akun.password is None:
                print(f"{'='*50}\nData Saat Ini Kosong, Tidak Dapat Save!")
            else:
                print(f"{'='*50}")
                nama_file = input("Silahkan Masukkan Nama File : ") + ".txt"
                if not os.path.exists(nama_file):
                    with open(nama_file, mode="a") as file:
                        file.write(f"+{'='*99}\n")
                        file.write(f"|Data yang tersimpan\n")
                        file.write(f"+{'='*99}\n")
                    with open(nama_file, mode="a") as file:
                        file.write(f"Nama          : {detail_akun.nama}\n")
                        file.write(f"Email         : {detail_akun.email}\n")
                        file.write(f"Password      : {detail_akun.password}\n")
                        file.write(f"+{'='*99}\n")
                else:
                    with open(nama_file, mode="a") as file:
                        file.write(f"Nama          : {detail_akun.nama}\n")
                        file.write(f"Email         : {detail_akun.email}\n")
                        file.write(f"Password      : {detail_akun.password}\n")
                        file.write(f"+{'='*99}\n")
                print("Berhasil!")
                detail_akun = Detail()
        case 5:
            if detail_akun.nama != None:
                print("Detail anda sudah ada sebelumnya apa anda yakin ingin menimpanya dengan data baru?")
                lanjut = input("Lanjut/Tidak ? = ")
                if lanjut == "Lanjut":
                    pass
                elif lanjut == "Tidak":
                    continue
                else:
                    print("Inputan salah! Keluar dari Program")
                    break
            print(f"{'='*50}")
            nama = Nama()
            email = Email()
            password = Password()
            if password is None:
                password = Password()
            detail_akun.BuatNama(nama=nama)
            detail_akun.BuatEmail(email)
            detail_akun.BuatPassword(password)
        case 6:
            print(f"{'='*50}\nSampai Jumpa Lagi")
            break
        case _:
            print(f"Jangan Asal Ketik Opsi!")
            break