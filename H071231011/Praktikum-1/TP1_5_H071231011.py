print("Konversi Detik ke Jam")
detik = int(input("Masukkan Detik : "))

#Rumus
jam = detik//3600
sisa_detik = detik % 3600
menit = sisa_detik//60
detik = sisa_detik % 60

print(f"{jam:02d}:{menit:02d}:{detik:02d}")

