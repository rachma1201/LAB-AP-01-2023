kata = input("Masukkan kata = ")
panjang= len(kata)
result = ""         
if panjang % 2 == 0:
    result += kata[0] + kata[panjang/2-1] + kata[panjang/2] + kata[-1]
else:
    result += kata[0] + kata[panjang//2] + kata[-1]
print(result)
