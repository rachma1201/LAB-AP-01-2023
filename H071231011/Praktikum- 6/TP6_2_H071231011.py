def cek_duplikat (angka1, angka2):
    duplikat= tuple(set(angka1) & set(angka2))
    if duplikat:
        return f"Terdapat {len(duplikat)} buah yaitu {duplikat}"
    else: 
        return "Tidak ada duplikasi ditemukan"
    
nilai1 = [int(x) for x in input('Masukkan array ke-1 : ').split()]
nilai2 = [int(x) for x in input('Masukkan array ke-2: ').split()]
print(cek_duplikat(nilai1, nilai2))