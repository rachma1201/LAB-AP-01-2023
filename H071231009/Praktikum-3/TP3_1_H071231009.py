input_suku= int(input())
a = 0  
b = 1 
for i in range (input_suku):
    print(a, end = " ")
    jumlah = a+b
    a = b
    b = jumlah 