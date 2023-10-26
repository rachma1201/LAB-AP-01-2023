array1 = set(map(int, input("Masukkan Array Ke-1 : ").split()))
array2 = set(map(int, input("Masukkan Array Ke-2 : ").split()))
irisan = tuple(array1&array2)
jumlah = len(irisan)

if jumlah > 1:
    print(f"Terdapat {jumlah} buah duplikat yaitu {irisan}")
elif jumlah == 1:
    print(f"Terdapat {jumlah} buah duplikat yaitu ({irisan[0]})") 
else:
    print("Tidak ada duplikat yang ditemukan")