print("Menghitung Luas Permukaan dan Keliling Segitiga")
x = float(input("Panjang sisi X : "))
y = float(input("Panjang sisi Y : "))

z = (x**2 + y**2)**0.5

luas = 0.5*x*y
keliling = x+y+z
print(f"luas segitiga tersebut adalah {luas:.2f}")
print(f"keliling segitiga tersebut adalah {keliling:.2f}")