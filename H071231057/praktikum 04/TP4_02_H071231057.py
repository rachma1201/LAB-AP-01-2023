def is_palindrome(word: str) -> str:
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil
    word = word.lower()
    
    # Mengecek apakah kata adalah palindrom
    if word != word[::-1]:
        return "Bukan Palindrom"
    return "Palindrom"

# Test Case 1
print(is_palindrome("Ayam"))  # Output: Palindrom

