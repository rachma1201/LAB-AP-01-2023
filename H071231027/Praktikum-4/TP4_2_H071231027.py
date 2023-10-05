def palindrom(n: str)->str:
        n = n.lower()
        balik = n[::-1]
        if n == balik :
            return "Palindrom"
        return "Bukan Palindrom"


print("\nTest 1")
print(palindrom("Katak"))

print("\nuji")
n = input("Cek Kata = ").lower()
print(palindrom(n))