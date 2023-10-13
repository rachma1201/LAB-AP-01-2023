def ATH(karakter):
    panjang = len(karakter)
    if panjang < 3:
        return "String input terlalu pendek."
    
    awal = karakter[0]
    tengah_ganjil = karakter[panjang // 2]
    tengah_genap = karakter [(panjang//2)-1]+karakter [panjang //2]
    akhir = karakter[-1]
    if panjang %2 == 0: 
        hasil = f"{awal}{tengah_genap}{akhir}"

    else:
        hasil = f"{awal}{tengah_ganjil}{akhir}"  

    return hasil

kata = input("Masukkan kata: ")
kata = kata.replace(" ","")
hasil_string = ATH(kata)
print("String baru:", hasil_string)