def stringPermutation(kata):
    try:
        kata_panjangnya = len(kata)
        for _ in range(kata_panjangnya):
            kata = kata[-1] + kata[:-1]
            print(kata, end= " | ")
    except TypeError:
        print("input harus berupa string")

stringPermutation("MOBIL")