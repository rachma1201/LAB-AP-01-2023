class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk ):
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan
        self.__ipk = ipk
    def get_name(self):
        return self.__nama
    def set_name(self, nama):
        self.__nama = nama
    def get_nim(self):
        return self.__nim
    def set_nim(self, nim):
        self.__nim = nim
    def get_jurusan(self):
        return self.__jurusan
    def set_jurusan(self, jurusan):
        self._jurusan = jurusan
    def get_ipk(self):
        return self.__ipk
    def set_ipk(self, ipk):
        self._ipk = ipk
    def Tampilkan_info(self):
        print(f"{'Nama':<8} : {self.__nama}")
        print(f"{'Nim':<8} : {self.__nim}")
        print(f"{'Jurusan':<8} : {self.__jurusan}")
        print(f"{'IPK':<8} : {self.__ipk}")
    def Hitung_predikat(self):
        if self.__ipk >= 3.5:
            return "Cumlaude"
        elif self.__ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.__ipk >= 2.5:
            return "Memuaskan"
        elif self.__ipk >= 2.0:
            return "Cukup"
        elif self.__ipk < 2.0:
            return "Kurang"
mahasiswa = Mahasiswa("Resky", "H071231009", "MIPA" , 3.8  )
mahasiswa.get_name()
mahasiswa.get_nim()
mahasiswa.get_jurusan()
mahasiswa.get_ipk()
mahasiswa.Tampilkan_info()
print(f"{'Predikat':<8} :", mahasiswa.Hitung_predikat())