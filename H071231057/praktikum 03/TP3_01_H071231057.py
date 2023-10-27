n = input()

# Langkah 2: Menggunakan Loop for untuk Menghitung Deret Fibonacci
a, b = 0, 1
for i in range(int(n)):
    print(a, end=' ')
    a, b = b, a+b

# Langkah 3: Menampilkan Deret Fibonacci
print()