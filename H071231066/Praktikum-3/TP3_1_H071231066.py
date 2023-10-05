n = int(input("n = ")) #nilai n
if n < 0:
    print("Bukan Fibonacci") 
u1 = 0 #suku pertama fibonacci
u2 = 1 #suku kedua fibonacci
for i in range(n): #Perulangan sebanyak n yang diinput
    print(u1, end=" ")  #kalau kita input 0 dia tidak masuk perulangan karena 0 perulangan, kalau 1 baru berulang
    u3 = u1 + u2        #u3 itu suku berikutnya
    u1 = u2             #u1 dan u2 itu dua suku sebelumnya bukan  dua suku pertama  
    u2 = u3             #jadinya u1 dan u2 akan berubah nilainya yang awalnya 0 dan 1 akan berubah sesuai berapa banyak perulangan yang akan terjadi
