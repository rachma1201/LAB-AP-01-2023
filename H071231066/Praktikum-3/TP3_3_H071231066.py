while True: #pakai While true karena perulangan, dia akan berulang jika nilainya bernilai benar atau true, dalam hal ini true itu nilainya angka
    try: #disini dia try dan jika kodenya berhasil maka dia berulang jika eror ke bagian except
        derajat = float(input("Masukkan derajat = "))
        if 0 <= derajat < 360:
            total_detik = int(derajat * 240 + 21600) % 86400
            #Kenapa derajat dikali 240? karena 1 derajat sama dengan 240 detik
            #Kenapa ditambah lagi 21600? 21600 itu detik, karena disini ada syarat jika 0 derajat itu sama dengan jam 6 pagi, 21600 detik itu sama dengan 6 jam
            #Kenapa setelah itu di modulo dengan 86400?
            #Karena kita ingin agar format jamnya tetap 24,misal 25 jam otomatis itu jam 1 dini hari
            #Tercetak bukan 25:00:00, tapi 01:00:00
            #Pada intinya 86400 itu jumlah detik dalam sehari full (24 jam)
            #kita cari sisa hasil baginya (modulo) karena formatnya 24 jam
            jam = total_detik // 3600 #disini total detik dibagi dengan 3600 detik (1 jam)
            sisa = total_detik % 3600 #disini kita ingin tahu sisa detiknya
            menit = sisa // 60 #terus dbagian ini kita mencari tau menitnya dengan cara sisa detik tadi dibagi 60 detik (1 menit)
            detik = sisa % 60 #terus disini kita ingin tahu berapa detik dari sisa detik tadi (mirip dengan praktikum 1)

            if 4 <= jam < 12: #jika jamnya itu pukul 4-11 maka waktunya pagi
                waktu = "Pagi" 
            elif 12 <= jam < 15: #jika jamnya di rentang pukul 12-14 maka waktunya siang
                waktu = "Siang"
            elif 15 <= jam < 18: #jika 
                waktu = "Sore"
            else:
                waktu = "Malam"

            print(f"Selamat {waktu}\n{jam:02}:{menit:02}:{detik:02}")
        else:
            print("End of File")
    except: #dibagian ini jika misalnya inputannya meminta angka, namun kita memberinya huruf (string) otomatis eror
        print("End of File")
        break #keluar dari perulangan, tanpa break ini walau eror dia tetap berulang, akan meminta inputan lagi (infinite loop)
    
