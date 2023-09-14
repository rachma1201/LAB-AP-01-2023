#Tugas 3 Persamaan Kuadrat
a = int(input("Input a = "))
if a == 0:
        print("Input a tidak boleh 0 !")
        exit()
b = int(input("Input b = "))
c = int(input("Input c = "))

# Agar Lebih Simple dan takutnya terjadi eror
b1 = b ** 2
a1 = 2 * a
ac = 4 * a * c

# Rumus Persamaan Kuadratnya
x1 = (- b + ((b1 - ac)**0.5))/a1
x2 = (- b - ((b1 - ac)**0.5))/a1

print(f'x1 = {x1:.2f}')
print(f'x2 = {x2:.2f}')