print("INFORMASI DAYA LISTRIK DAN TOTAL TAGIHAN\n----------------------------------------")
GOLONGAN  = (input("MASUKKAN GOLONGAN LISTRIK ANDA ANDA : "))
DAYA      = float(input("MASUKKAN DAYA LISTRIK ANDA : "))
PEMAKAIAN = float(input("MASUKKAN JUMLAH PEMAKAIAN ANDA :"))
match GOLONGAN :
    case "R1"  :
        if DAYA == 900     :
            X1  = (PEMAKAIAN) * (1352)  
            print(f"JUMLAH  PEMAKAIAN ANDA ADALAH SEBESAR RP.{X1:.1f}"   )
        elif DAYA == 1300  :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1444.70))
        elif DAYA == 2200  :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1444.70))
        else :
            print("INVALID INPUT")
    case "R2"  :
        if DAYA >= 3500 and DAYA <= 5500 :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1699.53))
    case "R3"  :
        if DAYA >= 6600 :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1699.53))
    case "B2"  :
        if DAYA >= 6600 and 20000 :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1444.70))
    case "B3"  :
        if DAYA >=20000  :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1114.74))
    case "I3"  :
        if DAYA >= 20000 :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1314.12))
    case "P1"  :
        if DAYA >=6.600 and DAYA <= 20000 :
            print("JUMLAH PEMAKAIAN ANDA ADALAH SEBESAR RP." , int(PEMAKAIAN) * (1523.28))
    case other :
        print("INVALID INPUT")
