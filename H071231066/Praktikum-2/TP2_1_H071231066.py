jenis_kelamin = int(input("Pilih Gender Anda \n1. Pria\n2. Wanita\n= "))
if jenis_kelamin >= 3 or jenis_kelamin <= 0:
    print("Tidak Valid!")
    exit()
tinggi = int(input("Masukkan tinggi badan (cm) = "))
berat = float(input("Masukkan berat badan (kg)= "))
bmi = berat/((tinggi/100)**2)

if jenis_kelamin == 1:
    if bmi < 18:
        print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
    elif bmi >= 18 and bmi < 24:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif bmi >= 24 and bmi < 27:
        print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    elif bmi >= 27:
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}");
elif jenis_kelamin == 2:
    if bmi < 17:
        print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
    elif bmi >= 17 and bmi < 24:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif bmi >= 24 and bmi < 28:
        print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    elif bmi >= 28:
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}");