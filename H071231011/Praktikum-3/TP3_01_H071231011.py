n = int(input("Masukkan nilai N :  "))
if n <= 0:
    print("Bukan fibonacci!") #Syarat Bilangan Fibonacci tidak mines atau 0!
else:
    s1 = 0 
    s2 = 1 
    print(s1, s2, end=" ") #Fungsi End yaitu agar outputnya terus ke kanan bukan membuat line baru
    for i in range(n-2): 
        s3 = s1 + s2   
        s1, s2 = s2, s3 
        print(s3, end=" ")

["Bilangan fibonacci adalah bilangan yang suku berikutnya ditentukan"]
["dari penjumlahan dua suku sebelumnya"]

(" NILAI N ITU SUKU BERAPA")
