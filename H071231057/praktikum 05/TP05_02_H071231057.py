def gabungan(string) :
    if len(str(string)) < 3:
        return "MASUKKAN STRING YANG ADA NILAI TENGAH!"
        
    if len(str(string)) % 2 == 0 :
        HURUF_PERTAMA = (string[0])
        HURUF_TENGAH  = string[len(string) //2 -1 ] +  string[len(string) //2 ]
        HURUF_AKHIR   = (string[-1])
    
    elif len(str(string)) % 2 != 0 :
        HURUF_PERTAMA = (string[0])
        HURUF_TENGAH  = string[len(string) //2]
        HURUF_AKHIR   = (string[-1])  

    GABUNGAN_STRING1 = HURUF_PERTAMA + HURUF_TENGAH + HURUF_AKHIR
   
    return GABUNGAN_STRING1
string = input("MASUKKAN KATANYA : ")
print(gabungan(string))




# a = int(input())

# if a // 2  == 0:
#   print(a+10)
# elif a//2 != 0 :
#   print(a//2)