n = int(input())
a, b= 0, 1
if n > 0:
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
else:
    print("0")


         
        