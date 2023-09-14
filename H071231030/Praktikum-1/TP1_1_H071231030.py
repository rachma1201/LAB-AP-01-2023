#Nomor 1
x = float (input("panjang sisi x :"))
y = float (input("panjang sisi y :"))
z = (x**2+y**2)**0.5

luas = 0.5*x*y
keliling = x+y+z

print(f"Luas Permukaan = {luas:.2f}")
print(f"Keliling = {keliling:.2f}")