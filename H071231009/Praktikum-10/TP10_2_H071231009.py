class Bentuk:
    def __init__(self, nama):
        self.nama = nama

    def menghitung_luas(self):
        pass

class Bulat(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self._radius = radius

    def menghitung_luas(self):
        return 3.14 * self._radius **2

    def getradius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius

class Segitiga(Bentuk):
    def __init__(self, nama, alas, tinggi):
        super().__init__(nama)
        self._alas = alas
        self._tinggi = tinggi

    def menghitung_luas(self):
        return 1/2 * self._alas * self._tinggi
    
    def getalas(self):
        return self._alas
    
    def set_alas(self, alas):
        self._alas = alas
    
    def gettinggi(self):
        return self._tinggi
    
    def set_tinggi(self, tinggi):
        self._tinggi = tinggi
  
bulat = Bulat("Lingkaran", 5)
print(f"before luas lingkaran: {bulat.menghitung_luas()}")
bulat.set_radius(6)
# print(f"radius: {bulat.getradius()}")
print(f"after luas lingkaran: {bulat.menghitung_luas()}")
print("="*50)
segi_tiga = Segitiga("Segitiga", 5, 4)
print(f"before luas segitiga: {bulat.menghitung_luas()}")
segi_tiga.set_alas(6)
segi_tiga.set_tinggi(8)
print(f"after luas segitiga: {segi_tiga.menghitung_luas()}")