print("Konversi Suhu dari Celsius ke Kelvin, Reamur, Fahrenheit")
#input suhu dalam celsius
celsius_input = int(input("masukkan Suhu dalam Celsius : "))       

kelvin = int(celsius_input + 273.15)
reamur = int(celsius_input * 4/5)
fahrenheit = int((celsius_input *9/5) + 32)
#hasil konversi
print(f"Hasil konversi dari suhu {celsius_input} derajat Celsius ke Kelvin adalah: {kelvin}K")
print(f"Hasil konversi dari suhu {celsius_input} derajat Celsius ke Reamur adalah: {reamur}R")
print(f"Hasil konversi dari suhu {celsius_input} derajat Celsius ke Fahrenheit adalah : {fahrenheit}F")
