kata = input("Masukkan kata : ")
p = len(kata)
if p % 2 == 0:
    kata = kata[0] + kata[p//2-1] + kata[p//2] + kata[-1]
else:
    kata = kata[0] + kata[p//2] + kata[-1]
print(kata)