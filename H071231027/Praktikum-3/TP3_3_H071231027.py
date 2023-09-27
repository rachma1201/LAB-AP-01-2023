while True:
    try :
        derajat = float(input("\nMasukkan posisi matahari atau bulan (derajat) = "))
       
        if 0 <= derajat < 360:
            menit = (derajat / 360) * 24 * 60 
            jam = (menit // 60) + 6
            if jam >= 24:
                jam %= 24
            menit %= 60
            detik = (menit * 60) % 60
            menit = int(menit)
    
                
            if  0 <= jam < 10:
                print ("\nSelamat Pagi")
            elif 10 <= jam < 15:
                print ("\nSelamat Siang")
            elif 15 <= jam  < 18:
                print ("\nSelamat Sore")
            elif 18 <= jam < 24 :
                print ("\nSelamat Malam")

            print (f"{jam:02.0f}:{menit:02.0f}:{detik:02.0f}\n")
        else:
            print("\nEnd of File")
    except:
        print("\nEnd of File")
        break




    
