#Nomor 4
inputan = input("Masukkan karakter = ")

huruf_kapital = (inputan.isupper())
huruf_kecil = (inputan.islower())
angka = (inputan.isdigit())

print(f"karakter huruf kapital? {huruf_kapital}")
print(f"karakter huruf kecil? {huruf_kecil}")
print(f"karakter angka? {angka}")
