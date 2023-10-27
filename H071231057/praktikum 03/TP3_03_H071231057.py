while True:
    try:
        M = float(input("Masukkan sudut matahari (0 ≤ M < 360): "))
        if 0 <= M <= 360:
            # Konversi sudut ke jam
            jam = int(M // 360 + 6)

            # Hitung jam, menit, dan detik
            sisa_sudut = M * 24 % 3600
            menit = int(sisa_sudut % 3600)// 60
            detik = int((sisa_sudut % 60) )

            # Tentukan waktu hari
            if 0 >= jam < 11:
                waktu_hari = "Selamat Pagi"
            elif  12 >= jam < 14:
                waktu_hari = "Selamat Siang"
            elif 15 >= jam < 18:
                waktu_hari = "Selamat Sore"
            elif jam >= 18 :
                waktu_hari = "Selamat Malam"
            else :
                "selamat subuh"
            

            # Cetak hasil
            print(f"{waktu_hari}, {jam:02d}:{menit:02d}:{detik:02d}")
        else:
            print("Input tidak valid. Harap masukkan angka antara 0 hingga 360.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    except EOFError:
        break