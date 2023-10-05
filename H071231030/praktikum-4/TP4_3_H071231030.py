def terbesar(x):
    terbesar = x[0]
    for i in x:
        if i > terbesar:
            terbesar = i
    return terbesar

x = [12, 43, 27, 80, 9]
print(terbesar(x))