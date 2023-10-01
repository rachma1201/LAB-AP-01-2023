print("Pengujian Jenis Karakter")
print("-"*25)
karakter= input("Karakter = ")

huruf_kapital = karakter >= 'A' and karakter <= 'Z'
huruf_kecil = karakter >= 'a' and karakter <= 'z'
angka = karakter >= '0' and karakter <= '9'

print("huruf kapital?", huruf_kapital )
print("huruf kecil?", huruf_kecil )
print("angka?", angka )

