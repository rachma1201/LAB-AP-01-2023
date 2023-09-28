y = int(input())
x = int(input())
kembalian = x-y
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000 ]
for nilai in pecahan:
    jumlah = kembalian // nilai
    kembalian -= jumlah * nilai
    print(f"{jumlah} uang sejumlah RP.{nilai}")