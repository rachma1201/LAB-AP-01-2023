String1 = input("Masukkan String 1 : ")
String2 = input("Masukkan String 2 : ")

String2 = "".join(reversed(String2))
x = ""
panjang = min(len(String1), len(String2))
for i in range(panjang):
    x += String1[i] + String2[i]
x += String1[panjang:] + String2[panjang:]

print(x)