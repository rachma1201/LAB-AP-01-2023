def palindrom(kata: str)-> str:
    kata = kata.lower().replace(" " , "")

    if kata == kata [::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
kata = str("saya") 
print(palindrom(kata))


