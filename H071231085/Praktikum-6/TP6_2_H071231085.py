# array1 = set(list(map(int,(input("Input array ke-1 : ").split()))))
# array2 = set(list(map(int,(input("Input array ke-2 : ").split()))))

# x = array1.intersection(array2)
# x = tuple(x)
# print(f"Terdapat {len(x)} buah duplikat yaitu {x}")


array1 = set(list(map(int,(input("input array ke-1 : ").split()))))
array2 = set(list(map(int,(input("input array ke-2 : ").split()))))

a = array1.intersection(array2)
a = tuple(a)
print(f"terdapat (len{a}) buah duplikat yaitu {a}")