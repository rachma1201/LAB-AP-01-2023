word1 = input("Masukkan kata pertama: ").replace(" ", "").lower()
word2 = input("Masukkan kata kedua: ").replace(" ", "").lower()

if len(word1) != len(word2):
    print(False)
    exit()

for char in word1:
    word1.count(char)
for char in word2:
    word2.count(char)

if word1.count(char) == word2.count(char):
    print(True)
else:
    print(False)














# word2 = word2.replace(" ", "").lower()
# word1 = word1.replace(" ", "").lower()




# word1 = input("Masukkan kata pertama: ")
# word2 = input("Masukkan kata kedua: ")

# word2 = word2.replace(" ", "").lower()
# word1 = word1.replace(" ", "").lower()

# if len(word1) != len(word2):
#     print(False)
#     exit()
    
# Karakter1 = {}
# Karakter2 = {}

# for char in word1:
#     Karakter1[char] = 1
# for char in word2:
#     Karakter2[char] = 1

# if Karakter1 == Karakter2:
#     print(True)
# else:
#     print(False)