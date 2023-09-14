Celsius = int(input("Masukkan Suhu dalam Celcius = "))

#Konversi Celsius ke Fahrenheit
Fahrenheit = int(Celsius*9/5)+32

#Konversi Celsius ke Kelvin
Kelvin = int(Celsius + 273.15)

#Konversi Celsius ke Reamur
Reamur = int(Celsius*4/5)

print(f"Hasil konversi dari suhu {Celsius} ke Fahrenheit adalah : {Fahrenheit}F")
print(f"Hasil konversi dari suhu {Celsius} ke Kelvin adalah : {Kelvin}K")
print(f"Hasil konversi dari suhu {Celsius} ke Reamur adalah : {Reamur}R")