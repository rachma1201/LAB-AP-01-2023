while True:
    M = float(input())
    if 0 <= M < 360:
        break
    else: 
        print('End Of File')

Detik = int(M * 240) # 1 derajat sama dengan 4 menit (240 detik)

Jam = Detik // 3600 + 6
if Jam >= 24:
    Jam = Jam % 24
Menit = Detik % 3600 // 60
Detik = Detik % 60

if 6 <= Jam < 11:
    print("Selamat Pagi")
elif 11 <= Jam < 15:
    print("Selamat Siang")
elif 15 <= Jam < 18:
    print("Selamat Sore")
else:
    print("Selamat Malam")

print(f"{Jam:02}:{Menit:02}:{Detik:02}")