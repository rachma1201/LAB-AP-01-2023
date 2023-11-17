class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan 
        self.ipk  = ipk
    
    def tampilkan_info(self):
        print(f'''
====Data {self.nama}====
Nama     = {self.nama}
NIM      = {self.nim}
Jurusan  = {self.jurusan}
IPK      = {self.ipk}''')
    def hitung_predikat(self):
        predikat = ""
        if 3.5 <= self.ipk <= 4.0:
            predikat += "Cumlaude"
        elif 3.5 > self.ipk >= 3.0:
            predikat += "Sangat Memuaskan"
        elif 3.0 > self.ipk >= 2.5:
            predikat += "Memuaskan"
        elif self.ipk >= 2.0:
            predikat += "Cukup"
        elif 0.0 <= self.ipk < 2.0:
            predikat += "Kurang"
        else:
            predikat += "Tidak Valid"
        print(f'Predikat = {predikat}')

print("\n======Masukkan Data Mahasiswa======")
nama = input("Nama Mahasiswa = ")
nim = input("NIM = ")
jurusan = input("Jurusan = ")
ipk = float(input("IPK = "))
mahasiswa = Mahasiswa(nama, nim, jurusan, ipk)
mahasiswa.tampilkan_info()
mahasiswa.hitung_predikat()

