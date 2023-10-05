def permutasi_kata(kata):
    for i in range(len(kata)):
        kata = kata[-1] + kata[:-1]
        print(kata, end=" | ")

try:
    permutasi_kata("mobil")

except TypeError:
    print("Terjadi Error, kata harus berupa data atau string")