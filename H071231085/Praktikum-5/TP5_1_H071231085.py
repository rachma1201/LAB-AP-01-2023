# dictio = {"Nama : ", "Umur : ", "Alamat : "}
# print("Selamat datang untuk memulai silahkan input data anda")

# x = input("input nama :")
# dictio["Nama : "] = x
# y = int(input["Umur : "])
# dictio["Umur : "] = y
# z = input("input Alamat : ")
# dictio["Alamat : "]

# print("="*50)
# print(f"Selamat datang {dictio['Nama']}Silahkan pilihh opsi")


def gabung_str(s1, s2):
    s3 = ''
    len_s1, len_s2 = len(s1), len(s2)
    s2 = s2[::-1] 
    for i in range(max(len_s1, len_s2)): 
        if i < len_s1: 
            s3 += s1[i]  
        if i < len_s2:
            s3 += s2[i]
    return s3
s1 = input("Masukkan kata 1: ")
s2 = input("Masukkan kata 2: ")
print(gabung_str(s1, s2))
