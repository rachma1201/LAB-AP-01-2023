def terbesar(x):
    terbesar = x[0]
    for i in x:
        if terbesar < i:
            terbesar = i
    return terbesar
x = [0, 2, 1, 3, 5, 2, 6, 4, 7, 8, 5, 5]
print(terbesar(x))
