def stringPermutation(n):
    try:
        if n.isnumeric():
            raise TypeError()
        else:
            huruf = n
            for i in range(len(n)):
                balik = huruf[-1] + huruf[0:-1]
                print(balik, end=" | ",)
                huruf = balik
    except :
        print("\nType Error")

print("\ntes case 1")
stringPermutation("Ayam")

print("\ntes case 2")
stringPermutation("Mobil")

print("\ntes case 3")
stringPermutation(123)

print("uji")
n = input("Masukkan Kata = ")
stringPermutation(n)