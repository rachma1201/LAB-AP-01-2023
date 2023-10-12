s1 = input("masukkan kata: ")
s2 = input("masukkan kata: ")[::-1]
hasil = ""
i = 0
while i < len(s1) and i < len(s2):
    hasil += s1[i] + s2[i]
    i += 1
hasil += s1[i:] + s2[i:]
print(hasil) 
