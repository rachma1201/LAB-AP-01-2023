#programn konversi waktu dari detik ke jam:menit:detik

print('konversi detik ke jam')
z = int(input('masukanjumlah detik : '))

jam = z // 3600
z %= 3600
menit = z // 60
z %= 60 
detik = z % 60 

print(f'{jam:2d}:{menit:02d}:{detik:02d}')