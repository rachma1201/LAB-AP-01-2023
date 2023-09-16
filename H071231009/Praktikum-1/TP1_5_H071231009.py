print("konversi detik ke jam")

detik = int(input("masukkan jumlah detik: "))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

hasil_konversi = f"{jam:02}:{menit:02}:{detik:02}"

print(hasil_konversi)

