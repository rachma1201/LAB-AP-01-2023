#Program Menghitung Permukaan Luas Dan Keliling Segitiga
import math
print("Menghitung Permukaan Luas dan Keliling Segitiga")
x = float(input("Masukkan Panjang Sisi X : "))
y = float(input("Masukkan Panjang Sisi Y : "))
z = math.sqrt(x**2 + y**2) #Karena input hanya menerima sisi X dan Y, 
#tapi untuk cari keliling dibutuhkan sisi z maka menggunakan rumus pythagoras

#Rumus 
Luas = ((1/2 * y) * x)
Keliling = (x + y + z)

print(f"Luas dari segitiga : {Luas:.2f}")
print(f"Keliling dari segitiga : {Keliling:.2f}")
