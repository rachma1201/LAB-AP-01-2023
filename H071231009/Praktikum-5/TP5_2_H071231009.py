input_kata = input("Masukkan kata: ").replace(" ","")
panjang = len(input_kata)
if panjang < 3 :
    print("kata terlalu pendek")
elif panjang % 2 == 0:
    awal = input_kata[0]
    tengah = input_kata[panjang//2-1]+input_kata[panjang//2]
    akhir = input_kata[-1]
else:
    awal = input_kata[0]
    tengah = input_kata[panjang//2]
    akhir = input_kata[-1]
print(f"{awal}{tengah}{akhir}")