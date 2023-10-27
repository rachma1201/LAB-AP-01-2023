print("BMI (PENETUAN KATEGORI JENIS BODY MAX INDEX BERDASARKAN GENDER)")
print("----------------------------------------------------------------")
import math
print("KET. 1 = PRIA\n     2 = WANITA")
GENDER = input("TOLONG MASUKKAN GENDER ANDA : ")
if GENDER == "1" : 
    BB     = float(input("MASUKKAN BERAT BADAN ANDA (KG) :" ))
    TB     = float(input("MASUKKAN TINGGI BADAN ANDA (M) :"))
    BMI    = float(BB / TB**2 )
    if BMI <18 :
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : UNDERWEIGHT")
    elif BMI >=18 and BMI <23.9 : 
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : NORMAL")
    elif BMI >=24 and BMI <= 26.9 :
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : OVERWEIGHT")
    else :
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : OBESE")
elif GENDER == "2" :
    BB     = float(input("MASUKKAN BERAT BADAN ANDA (KG) :" ))
    TB     = float(input("MASUKKAN TINGGI BADAN ANDA (M) :"))
    BMI    = float(BB / TB**2 )
    if BMI <17 :
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : UNDERWEIGHT")
    elif BMI >=17 and BMI <23.9 : 
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : NORMAL")
    elif BMI >=24 and BMI <= 27.9 :
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : OVERWEIGHT")
    elif BMI >= 28 :
        print(f"BMI ANDA ADALAH" , '%.2f' % (BMI) , "DENGAN KATEGORI : OBESE")

