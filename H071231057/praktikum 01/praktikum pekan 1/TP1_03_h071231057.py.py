import math #import math untuk memancing math.sqrt atau akar

# Memasukkan koefisien dari nilai
a = float(input("Masukkan Nilai dari a: "))
b = float(input("Masukkan Nilai dari b: "))
c = float(input("Masukkan Nilai dari c: "))
#Disini pake float, karena int cuma bisa menampung bil.bulat
#Sementara hasil dari akar atau koefisien bisa saja pecahan atau desimal.

# Menghitung diskriminan
diskriminan = b**2 - 4*a*c

# Mengecek jika diskriminan positif, nol, atau negatif
if diskriminan > 0:
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print("Solusi dua akar nyata:")
    print("x1 =", x1)
    print("x2 =", x2)
    #Solusi ini terpakai ketika akar atau import mathnya bisa diakarkan yaitu hasil d lebih dari nol
elif diskriminan == 0:
    x1 = -b / (2*a)
    print("Solusi satu akar nyata:")
    print("x1 =", x1)
#X1 DAN X2 SAMA, JADI KITA PAKE X1 SAJA
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(abs(diskriminan)) / (2*a)
    print("Solusi akar kompleks:")
    print("x1 =", realPart, "+", imaginaryPart, "i")
    print("x2 =", realPart, "-", imaginaryPart, "i")
#real part itu bilangan rill dan imaginary itu ku asumsikan bil.imaginer
#Bilangan imajiner didapat ketika akar atau math.sqrt yang dimasukkan adalah mines. contoh math.sqrt(-1).

#NOTE : KENAPA PAKE IF,ELIF DAN ELSE? KARENA HASILNYA TIDAK TENTU, MAKA HARUS ADA KONDISI LAIN DARI HASIL YANG KITA DAPAT
