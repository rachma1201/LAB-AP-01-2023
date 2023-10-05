def stringPermutation(kata):
    for i in range(len(kata)):
        kata = kata[-1] + kata[:-1]
        print(kata, end= " | ")
try:
    input_string = input("Masukkan string: ")
    if input_string.isdigit():
        raise TypeError
    
    hasil = stringPermutation(input_string)
    for x in hasil:
         print(x, end=" | ")
except TypeError:
    print("Error")