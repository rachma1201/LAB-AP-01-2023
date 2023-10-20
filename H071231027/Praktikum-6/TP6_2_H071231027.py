array1 =  set(map(int, input("\nInput array ke-1: ").split()))
array2 = set(map(int, input("Input array ke-2: ").split()))
irisan = tuple(array1&array2)
jumlah = len(irisan)
if jumlah == 1:
    print(f'Terdapat {jumlah} buah duplikat yaitu ({irisan[0]})\n')
elif irisan != ():
    print(f'Terdapat {jumlah} buah duplikat yaitu {irisan}\n')
else:
    print('Tidak ada duplikasi ditemukan\n')