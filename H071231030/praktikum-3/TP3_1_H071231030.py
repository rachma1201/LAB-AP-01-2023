n = int(input())

x = 0
y = 1

if n > 0:
    for i in range (n):
        print(x, end =" ")
        x,y = y, x + y
else:
    print("0")