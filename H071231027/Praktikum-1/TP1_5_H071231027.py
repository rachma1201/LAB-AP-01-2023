x = int(input("Masukkan jumlah detik: "))

jam = x//3600
sisa = x%3600
menit = sisa//60
detik = sisa%60

print (f"{jam:02}:{menit:02}:{detik:02f}")