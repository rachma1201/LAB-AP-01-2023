kelamin = int(input("Pilih Gender Anda\n1. Pria\n2. Wanita\n= "))
tinggi = int(input("Masukkan Tinggi Badan (cm) = "))
berat = float(input("Masukkan Berat Badan (kg) = "))
bmi = berat/((tinggi/100)**2)

match kelamin:
    case 1:
        if bmi < 18:
            print(f"Underweight dengan BMI : {bmi:.2f}")
        elif bmi >= 18 and bmi < 24:
            print(f"Normal dengan BMI : {bmi:.2f}")
        elif bmi >= 24 and bmi < 27:
            print(f"Overweight dengan BMI : {bmi:.2f}")
        elif bmi >= 27:
            print(f"Obese dengan BMI : {bmi:.2f}");
    case 2:
        if bmi < 17:
            print(f"Underweight dengan BMI : {bmi:.2f}")
        elif bmi >= 17 and bmi < 24:
            print(f"Normal dengan BMI : {bmi:.2f}")
        elif bmi >= 24 and bmi < 28:
            print(f"Overweight dengan BMI : {bmi:.2f}")
        elif bmi >= 28:
            print(f"Obese dengan BMI : {bmi:.2f}");
    case _:
        print("Data tidak valid!")