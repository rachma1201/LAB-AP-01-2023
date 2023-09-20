gender = int(input("Pilih Gender Anda \n 1. Pria \n 2. Wanita \n = "))
x = float(input("Masukkan tinggi badan (cm) : "))
y = float(input("Masukkan berat badan (kg) : "))

bmi = y/(x/100)**2
if gender == 1:
    if bmi < 18:
        kategori = "Underwight"
    elif 18 <= bmi < 23.9:
        kategori = "Normal"
    elif 24 <= bmi < 26.9:
        kategori = "Overweight"
    elif bmi >= 27:
        kategori = "Obese"
elif gender == 2:
    if bmi < 17:
        kategori = "Underwight"
    elif 17 <= bmi < 23.9:
        kategori = "Normal"
    elif 24 <= bmi < 27.9:
        kategori = "Overweight"
    elif bmi >= 28:
        kategori = "Obese"
print(f"Anda tergolong {kategori} dengan BMI {bmi:.2f}")

    