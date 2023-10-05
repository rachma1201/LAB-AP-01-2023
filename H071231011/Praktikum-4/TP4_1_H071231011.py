try:
    
    def permutasi(kata):
        permutasi = []
        for i in range(len(kata)):
            permutasi.append(kata)
            kata = kata [1:] + kata [0]
        permutasi.reverse()
        return permutasi 

    
#case1
    kata = "sepeda"
    hasil_permutasi = permutasi(kata)
    for hasil in hasil_permutasi:
        print(hasil, end = " | ")   
except TypeError:
    print("error, inputan harus berupa string!")   