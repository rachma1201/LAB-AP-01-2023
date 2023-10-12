input1 = input("masukkan kata: ")
input2 = input("masukkan kata2: ")[::-1]
hasil = ""
i = 0
while i < len(input1) and i < len(input2):
    hasil += input1[i] + input2[i]
    i += 1
hasil += input1[i:] + input2[i:]
print(hasil)