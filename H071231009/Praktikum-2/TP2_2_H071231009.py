x = input("Masukkan Input Pertama : ")
y = input("Masukkan Input Kedua : ")
z = input("Masukkan Input Ketiga : ")

if x == "vertebrado":
    if y == "ave":
        if z == "carnivora":
            print("agula")
        elif z == "onivoro":
            print("pomba")
        else:
            print("invalid input")
    elif y == "mamifero":
        if z == "onivoro":
            print("homem")
        elif z =="herbivoro":
            print("vaca")
        else:
            print("invalid input")
    else:
        print("invalid input")
elif x == "invertebrado":
    if y == "inseto":
        if z == "hematofago":
            print("pulga")
        elif z == "herbivoro":
            print("lagarta")
        else:
            print("invalid input")
    elif y == "anelideo":
        if z == "hematofago":
            print("sanguessuga")
        elif z == "onivoro":
            print("minhoca")
        else:
            print("invalid input")
    else:
        print("invalid input")
else:
    print("invalid input")