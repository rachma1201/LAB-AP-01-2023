x = float(input('Panjang sisi x = '))
y = float(input('Panjang sisi y= '))
z = (x**2+y**2)**0.5

Luas = (1/2)*y*x
Keliling = x + y + z

luas = f"{Luas:.2f}"
keliling = f"{Keliling:.2f}"

print(f"Luas Permukaan : {luas}")
print(f"Keliling : {keliling}")

