def palindrome(kata: str) -> str:
    kata = kata.lower()
    if kata == kata[::-1]: 
        return "Palindrome"
    else:
        return "Bukan Palindrome"

input_kata = input("Masukkan kata: ")
hasil = palindrome(input_kata)
print(hasil)