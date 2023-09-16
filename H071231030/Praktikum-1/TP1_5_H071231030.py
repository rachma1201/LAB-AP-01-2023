#Nomor 5
detik = int(input("Masukkan detik ="))

jam = detik // 3600
sisa = detik % 3600
menit = sisa // 60
detik = sisa % 60

print(f"{jam:02}:{menit:02}:{detik:02}")