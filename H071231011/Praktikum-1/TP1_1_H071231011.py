a = float(input("panjang sisi x : "))
b = float(input("panjang sisi y : "))

c = (a**2 + b**2)**0.5

#Rumus
luas = 0.5 * a * b
keliling = a + b + c

print(f"Luas segitiga: {luas:.2f}")
print(f"Keliling segitiga: {keliling:.2f}")
