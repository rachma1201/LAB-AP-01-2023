class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan
        self.__ipk = ipk
        
    def getNama(self):
        return self.__nama
    def setNama(self, nama):
        self.__nama = nama
    def getNim(self):
        return self.__nim
    def setNim(self, nim):
        self.__nim = nim
    def getJurusan(self):
        return self.__jurusan
    def setJurusan(self, jurusan):
        self.__jurusan = jurusan
    def getIPK(self):
        return self.__ipk
    def setIPK(self, ipk):
        self.__ipk = ipk
    
    def Tampilkan_info(self):
        return (f"Nama : {self.getNama()}\nNIM : {self.getNim()}\nJurusan : {self.getJurusan()}\nIPK : {self.getIPK()}")
    def Hitung_Predikat(self):
        if self.getIPK() >= 3.5:
            return "Cumlaude"
        elif 3.0 <= self.getIPK() < 3.5:
            return "Sangat Memuaskan"
        elif 2.5 <= self.getIPK() < 3.0:
            return "Memuaskan"
        elif 2.0 <= self.getIPK() < 2.5:
            return "Cukup"
        else:
            return "Kurang"
        
mahasiswa1 = Mahasiswa("Syahrini", "H071231066", "Sistem Informasi", 3.4)
mahasiswa2 = Mahasiswa("Fariz", "H071231011", "Teknik", 4.0)
print(mahasiswa1.Hitung_Predikat())
print(mahasiswa2.Tampilkan_info())