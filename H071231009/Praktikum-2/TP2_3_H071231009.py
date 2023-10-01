x = input("Golongan = ")
y = int(input("Daya = "))
z = int(input("Pemakaian = "))

if x == "R1":
    if y == 900:
        tarif = 1352 * z
    elif y == 1300:
        tarif = 1444.70
    elif y == 2200:
        tarif = 1444.70 * z
elif x == "R2" and 3500 <= y <= 5500:
        tarif = 1699.53 * z
elif x == "R3" and y >= 6600:
        tarif = 1699.53 * z
elif x == "B2" and 6600 <= y <= 200000:
        tarif = 1444.70 * z
elif x == "B3" and y > 200000:
        tarif = 1114.74 * z
elif x == "I3" and y >= 200000:
        tarif = 1314.12 * z
elif x == "P1" and 6600 <= y <= 200000:
        tarif = 1523.28 * z
else:
    print("data tidak valid")
    exit()
tagihan_baru = f"{tarif:,.1f}".replace(",","x").replace(".",",").replace("x",".")
print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {tagihan_baru}")