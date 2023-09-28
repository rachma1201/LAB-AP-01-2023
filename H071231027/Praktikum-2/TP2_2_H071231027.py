x = input("Masukkan Input Pertama : ")
if x != "vertebrado" and "invertebrado":
    print("invalid input")
    exit()
    
y = input("Masukkan Input Kedua : ")
if y != "ave" and "mamifero" and "inseto" and "anelido":
    print("invalid input")
    exit()
    
z = input("Masukkan Input Ketiga : ")
if z != "carnivoro" and "onivoro"and "herbivoro" and "hematofoga":
    print("invalid input")
    exit()

match x, y, z:
    case "vertebrado", "ave", "carnivoro":
        print("aguia")
    case "vertebrado", "ave", "onivoro":
        print("pomba")
    case "vertebrado", "mamifero", "onivoro":
        print("homem")
    case "vertebrado", "mamifero", "herbivoro":
        print("vaca")
    case "invertebrado", "inseto", "hematofago":
        print("pulga")
    case "invertebrado", "inseto", "herbivoro":
        print("lagarta")
    case "invertebrado", "anelido", "hematofago":
        print("sanguessuga")
    case "invertebrado", "anelido", "onivoro":
        print("minhoca")
    case _:
        print("Invalid input")
        

