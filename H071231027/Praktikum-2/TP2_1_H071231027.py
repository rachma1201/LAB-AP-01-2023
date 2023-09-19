print("Pilih Gender Anda")
Gender = "Pria"
Gender2 = "Wanita"
print(f"1.{Gender}\n2.{Gender2}")

x = input("= ")
Tinggi_Badan = float(input("Tinggi badan (cm) : "))
Berat_Badan = float(input("Berat badan (kg) : "))


BMI = Berat_Badan/(Tinggi_Badan/100)**2

if (BMI < 18 and x == "1") or (BMI < 17 and x == "2"):
    print("Anda tergolong Underweight dengan BMI", round (BMI, 2), "kg/m")

elif (18 <= BMI < 24 and x == "1") or (17 <= BMI < 24 and x == "2"):
    print("Anda tergolong Normal dengan BMI", round (BMI, 2), "kg/m")

elif (24<= BMI < 27 and x == "1") or (24<= BMI < 28 and x == "2"):
    print("Anda tergolong Overweight dengan BMI", round (BMI, 2), "kg/m")

else: 
    (BMI >=27 and x == "1") or (BMI >=28 and x == "2")
    print("Anda tergolong Obese dengan BMI", round (BMI, 2), "kg/m")
