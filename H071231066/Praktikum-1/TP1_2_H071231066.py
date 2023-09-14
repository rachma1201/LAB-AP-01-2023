# Program Konveri Suhu dari Celcius
print("Konversi Suhu Dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
celcius = int(input("Masukkan Nilai Suhu Dalam Celcius : "))

# Rumus Konversi
k = int(celcius + 273.15)
r = int(4/5*celcius)
f = int((9/5*celcius)+32)

print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {k}K")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Reamur adalah : {r}R")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Fahrenheit adalah : {f}F")