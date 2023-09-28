while True:
    M = float(input())
    if 0 <= M < 360:
        break
    else:
        print("End Of File")
detik = int(M * 240) 
jam = detik // 3600 + 6
if jam >= 24:
    jam = jam % 24
menit = detik % 3600 // 60
detik = detik % 60
if 6 <= jam < 12:
    print("Selamat Pagi")  
elif 12 <= jam < 15:
    print("Selamat Siang")
elif 15<= jam < 18:
    print("Selamat Sore")
else:
    print("Selamat Malam")
print(f"{jam:02d}:{menit:02d}:{detik:02d}")