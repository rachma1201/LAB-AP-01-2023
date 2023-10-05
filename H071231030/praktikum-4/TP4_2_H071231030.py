def Kata_Palindrome(kata):
    kata = kata.lower()
    balik = kata[::-1]
    if balik == kata:
        return "Merupakan Kata Palindrom"
    else:
        return "Bukan kata Palindrom"

print(Kata_Palindrome("kodok"))