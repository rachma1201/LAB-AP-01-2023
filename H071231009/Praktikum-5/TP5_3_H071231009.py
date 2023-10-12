kata1 = input("Masukkan kata pertama: ").replace(" ", "").lower()
kata2 = input("Masukkan kata kedua: ").replace(" ", "").lower()
if len(kata1) != len(kata2):
    anagram = False
else:
    frekuensi_kata1 = {}
    frekuensi_kata2 = {}

    for huruf in kata1:
        if huruf in frekuensi_kata1:
            frekuensi_kata1[huruf] += 1
        else: 
            frekuensi_kata1[huruf] = 1
            
    for huruf in kata2:
        if huruf in frekuensi_kata2:
            frekuensi_kata2[huruf] += 1
        else:
            frekuensi_kata2[huruf] = 1
    anagram = frekuensi_kata1 == frekuensi_kata2
print(anagram)