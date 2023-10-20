a = set(map(int,input("Input array ke-1: ").split()))
b = set(map(int,input("Input array ke-2: ").split()))
c = a & b
if len(c) > 1:
    print(f"terdapat {len(c)} buah duplikat yaitu {tuple(c)}")
elif len(c) == 1 :
    print(f"terdapat {len(c)} buah duplikat yaitu ({tuple(c)[0]})")
else:
    print("Tidak ada duplikasi ditemukan.") 