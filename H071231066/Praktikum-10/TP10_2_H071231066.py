from abc import ABC, abstractmethod
#Implementasian Metode Enkapsulasi

class Mobil:
    def __init__(self, warna, merk, ban):
        self.__warna = warna
        self.__merk = merk
        self.__ban = ban
    
    def getBan(self):
        return self.__ban
    def getWarna(self):
        return self.__warna
    def getMerk(self):
        return self.__merk
    def setWarna(self, warna):
        self.__warna = warna
    def setMerk(self, merk):
        self.__merk = merk
    def setBan(self, ban):
        self.__ban = ban
        
#Pengimplementasian Abstract Class, dan Polymorphism
class Bentuk(ABC):
    @abstractmethod
    def HitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def HitungLuas(self):
        return self.sisi ** 2
    
class Segitiga(Bentuk):
    def __init__(self, panjang, alas, tinggi):
        self.panjang = panjang
        self.alas = alas
        self.tinggi = tinggi
    def HitungLuas(self):
        return 1/2 * self.alas * self.tinggi
    
#Pengimplementasian Inheritance
class Meja:
    def __init__(self, name, kaki):
        self.name = name
        self.kaki = kaki
        
    def Bergeser(self):
        print(f"{self.name} Sedang bergeser ke suatu arah")

class Kursi(Meja):
    pass

persegi = Persegi(2)
print(persegi.HitungLuas())
segitiga = Segitiga(6, 4, 6)
print(segitiga.HitungLuas())


Honda = Mobil("Merah", "Honda", 4)
print(Honda.__dict__)
Honda.setBan(12)
print(Honda.__dict__)