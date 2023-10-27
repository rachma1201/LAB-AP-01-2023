def stringPermutation (word:str):
    
    try:
        # Loop melalui setiap karakter dalam kata
        for i in range(len(word)):
            # Geser karakter pertama ke posisi terakhir
            word = word[-1] + word[:-1]
            print(word, end="|")
    except TypeError :
        print("INPUTAN TIDAK VALID")

# Test Case 1
stringPermutation(input(""))

# Test Case 2
stringPermutation(input(""))