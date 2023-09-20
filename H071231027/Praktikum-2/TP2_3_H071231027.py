x = input("Golongan = ")
y = int(input("Daya = "))
z = int(input("Pemakaian = "))

if x == "R1" or x == "B2":
    if y == 900:
        total = z*1352
        
    elif (y == 1300 or y == 2200) or (6600 <= y <=200000):
        total = z*1444.70

    else:
        print("Data tidak valid")
        exit()
        
elif (x == "R2" or x == "R3") and (3500 <= y <= 5500 or y >= 6600): 
    total = z*1699.53
   
elif x == "B3" and y > 200000:
    total = z*1114.74
      
elif x == "I3" and y>=200000:
    total = z*1314.12
    
elif x == "P1" and 6600<= y <=200000:
    total = z*1523.28

else:
    print("Data tidak valid")
    exit()

format_total = f"{total:,.1f}".split(".")
integer_parts = format_total[0].replace(",",".")
decimal_parts = format_total[1]
print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {integer_parts},{decimal_parts}")
# print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {format_total}")



