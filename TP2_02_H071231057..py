print("KEYWORD FOR YOU!\n (1)VERTEBRADO\n (2)INVERTEBRADO\n (3)AVE\n (4)MAMIVERO\n (5)CARNOVORO -> AGUIA\n (6)ONIVORO -> POMBA\n (7)ONIVORO -> HOMEM\n (8)HERBIVORA -> VACA\n (9)INSETO\n (10)ANELIDEO\n (11)HEMATOFAGO -> PULGA - SANGUESSUGA\n (12)HERBIVORO -> LAGARTA\n (13)ONIVORO -> MINHOCA\n BEBERAPA OUTPUT TIDAK BERJALAN JIKA KITA MEMASUKKAN SINGLE CHARACTHER (MOHON UNTUK MEMASUKKAN INPUT YANG TERSTRUKTUR SESUAI TABEL)")
command = input("MASUKKAN INPUT : ")
match command:
    case "VERTEBRADO"                        :
        print("AVE,MAMIVERO")
    case "AVE"                               :
        print("CARNIVORA,ONIVORA")
    case "MAMIFERO"                          :
        print("ONIVORA,HERBIVORO")
    case "VERTEBRADO,AVE"                    :
        print("CARNIVORO,ONIVORO") 
    case "VERTEBRADO,AVE,CARNIVORO"          :
        print("AGUIA")
    case "VERTEBRADO,AVE,ONIVORO"            :
        print("POMBA")
    case "VERTEBRADO,MAMIVERO"               :
        print("ONIVORO,HERBIVORO")
    case "VERTEBRADO,MAMIVERO,ONIVORO"       :
        print("HOMEM")
    case "VERTEBRADO,MAMIFERO,HERBIVORO"     :
        print("VACA")
    case "INVERTEBRADO"                      :
        print("INSETO,ANELIDEO")
    case "INSETO"                            :
        print("HEMATOFAGO,HERBIVORO") 
    case "ANELIDEO"                          :
        print("HEMATOFAGO,ONIVORA")
    case "INVERTEBRADO,INSETO" :
        print("HEMATOFAGO")
    case "INVERTEBRADO,INSETO,HEMATOFAGO"    :
        print("PULGA")
    case "INVERTEBRADO,INSETO,HERBIVORO"     :
        print("LAGARTA")
    case "INVERTEBRADO,ANELIDEO" :
        print("HEMATOFAGO,ONIVORA")
    case "INVERTEBRADO,ANELIDEO,HEMATOFAGO"  :
        print("SANGUESSUGA")
    case "INVERTEBRADO,ANELIDEO,ONIVORA"     :
        print("MINHOCA")
    case other :
        print("INVALID INPUT, PLEASE TAKE A LOOK AND GIVE THE CORRECT COMMAND!")

 
