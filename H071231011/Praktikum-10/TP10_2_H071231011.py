class Bentuk:
    def __init__(self, nama):
        self.nama = nama

    def menghitung_luas(self): #abstrak
        pass

class Bulat(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self._radius = radius

    def radius(self):  #memanggil
        return self._radius
    
    def setradius(self, radius):    #mengubah
        self._radius = radius

    def menghitung_luas(self): #polymorphism 
        return 3.14 * self._radius ** 2 

class SegiEmpat(Bentuk):
    def __init__(self, nama, panjang_sisi):
        super().__init__(nama)
        self._panjang_sisi = panjang_sisi

    def getpanjangsisi(self):
        return self._panjang_sisi
    
    def setpanjangsisi(self, panjang_sisi):
        self._panjang_sisi = panjang_sisi


    def menghitung_luas(self):
        return self._panjang_sisi * self._panjang_sisi

bulat = Bulat("Lingkaran", 5)
segi_empat = SegiEmpat("Persegi", 4)

bentuk = [bulat, segi_empat]
luas = bulat.menghitung_luas()
radius = bulat.radius()
for i in bentuk:
    if isinstance(i, Bulat):
        print(f"Nama: {i.nama}, Luas: {luas}, Radius: {radius}")
    else:
        print(f"Nama: {i.nama}, Luas: {i.menghitung_luas()}")
