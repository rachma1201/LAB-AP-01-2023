#soal nomor 2 mengkonversi suhu celcius ke kelvin, reamur, dan farenheit : 
    
print('konversi suhu dari celcius ke kelvin, reamur, farenheit ')
c = int(input('masukan suhu dalam celcius: '))

K = int(c + 273) 
R = int(4/5 * c)
F = int((c* 9/5 + 32))

print (f'hasil konversi suhu dari {c} derajat celcius ke kelvin adalah: {K}k')
print (f'hasil konversi dari suhu {c} derajat celcius ke reamur adalah: {R}r')
print (f'hasil konversi dari suhu {c} derajat celcius ke farenheit adalah: {F}f') 