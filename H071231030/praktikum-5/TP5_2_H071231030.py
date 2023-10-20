kata = input("Masukkan String : ")
panjang = len(kata)
if panjang > 2:
    if panjang % 2 != 0:
        x = kata[0] + kata[panjang//2] + kata[-1]
    else:
        x = kata[0] + kata[panjang//2-1] + kata[panjang//2] + kata[-1]
    print(x)
else:
    print("Error")