# soal nomor 3 membuat program untuk menghitung solusi persamaan kuadrat 
a =  float(input('input a = '))
b =  float(input('input b = '))
c =  float(input('input c = '))

x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

if a ==0:
    print('error!! input nilai a != 0')
else:
    print(f'x1 = {x1: .2f}')
    print(f'x2 = {x2: .2f}')