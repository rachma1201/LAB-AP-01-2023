#soal nomor 1 menghitung  luas dan keliling segitiga X , Y , Z :
    
print ('menghitung luas dan keliling segita')
x = float(input('panjang sisi x : '))
y = float(input('panjang sisi y : '))
z = (x**2 + y**2)**0.5


L = x * y / 2
K = x + y + z
print(f'luas permukaan : {L: .2f}')
print(f'keliling : {K: .2f}')