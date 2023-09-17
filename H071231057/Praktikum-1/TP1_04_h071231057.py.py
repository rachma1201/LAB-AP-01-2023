#PENGUJIAN JENIS KARAKTER
KARAKTER = input("Masukkan Jenis Karakter : ")
HURUF_KAPITAL  = bool(False)
HURUF_KECIL    = bool(False)
KARAKTER_ANGKA = bool(False)

if KARAKTER.isupper():
    HURUF_KAPITAL  = True
if KARAKTER.islower():
    HURUF_KECIL    = True
if KARAKTER.isdigit():
    KARAKTER_ANGKA = True
else : 
    KARAKTER > r'A-Z' and r'a-z' 
    True
    
    


print(f"HURUF KAPITAL : {HURUF_KAPITAL :}\n HURUF KECIL :{HURUF_KECIL}\n KARAKTER ANGKA : {KARAKTER_ANGKA}\n JUMLAH KARAKTER : " ,  len(KARAKTER))

