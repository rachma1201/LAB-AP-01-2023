gender = int(input("Pilih Gender Anda \n1.Pria \n2.Wanita \n= "))
tinggi_badan = float(input("Masukkan tinggi badan (cm) : "))
berat_badan = float(input("Masukkan berat badan (kg) : "))

BMI = berat_badan / (tinggi_badan / 100)**2

if gender == 1:
    if  BMI < 18:
     print(f"anda tergolong Underweight dengan {BMI:.2f}")
    elif BMI >18 and BMI < 23.9:
      print(f"anda tergolong Normal dengan {BMI:.2f}")
    elif BMI >24 and BMI <26.9:
      print(f"anda tergolong Overweight dengan {BMI:.2f}")
    elif BMI >=27:
      print(f"anda tergolong Obese dengan {BMI:.2f}")

elif gender == 2:
    if BMI < 17:
       print(f"anda tergolong Underweight dengan {BMI:.2f}")
    elif BMI >17 and BMI <23.9:
        print(f"anda tergolong Normal dengan {BMI:.2f}")
    elif BMI >24 and BMI <27.9:
        print(f"anda tergolong Overweight dengan {BMI:.2f}")
    elif BMI >= 28:
        print(f"anda tergolong Obese dengan {BMI:.2f}")