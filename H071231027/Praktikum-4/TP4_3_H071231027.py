def maksimum(*args)-> int:
        max_num = args[0]
        for num in args:
            if num >= max_num:
                max_num = num 
        return max_num
        
print("\nTes case 1")
print(maksimum(-1, -2, -4, -6, -9, -3, -1, -9, -10))

print("\nTes case 2")
print(maksimum(0, -1, -90, -430, -23, -212, -34))


    




# input_num = input("Masukkan item = ").split()
# nums = [int(num) for num in input_num]
# print(maksimum(*nums))
    

