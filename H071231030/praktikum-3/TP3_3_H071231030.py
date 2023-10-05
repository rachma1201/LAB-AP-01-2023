while True:
    try:
        derajat = float(input("Masukkan nilai derajat = "))
        
        if 0 <= derajat < 360:
            menit = (derajat / 360) * 24 * 60
            jam = (menit // 60) + 6
            if jam >= 24 :
                jam %= 24
            detik = (menit * 60) % 60
            menit = menit % 60

            if 15 <= jam < 18:
                print("Selamat Sore")
            elif 6 <= jam < 10:
                print("Selamat Pagi")
            elif 10 <= jam < 15:
                print("Selamat Siang")
            elif 18 <= jam <= 24:
                print("Selamat Malam")
            
            print (f"{jam:02.0f}:{menit:02.0f}:{detik:02.0f}\n")
        else:
            print("\nEnd Of File")
    except:
        print("\nEnd Of File")
        break