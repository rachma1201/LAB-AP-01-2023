def anagram(karakter1, karakter2):
    karakter1 = karakter1.replace(" ", "").lower()
    karakter2 = karakter2.replace(" ", "").lower()
    
    if len(karakter1) != len(karakter2):
        return False

    simpan1 = {}
    simpan2 = {}

    for karakter in karakter1:
        if karakter in simpan1:
            simpan1[karakter] += 1
        else:
            simpan1[karakter] = 1
    
    # Menghitung jumlah kemunculan karakter dalam karakter2
    for karakter in karakter2:
        if karakter in simpan2:
            simpan2[karakter] += 1
        else:
            simpan2[karakter] = 1
    
    return simpan1 == simpan2

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
print(anagram(kata1, kata2))

