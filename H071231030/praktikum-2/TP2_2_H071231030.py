#Nomor 2
pertama = (input("masukkan input pertama :"))
kedua = (input("masukkan input kedua :"))
ketiga = (input("masukkan input ketiga :"))

match pertama,kedua,ketiga:
    case "vertebrado","ave","carnivoro":
        print("agula")
    case "vertebrado","ave","onivoro":
        print("pomba") 
    case "vertebrado","mamifero","onivoro":
        print("homem") 
    case "vertebrado","mamifero","herbivoro":
        print("vaca") 
    case "invertebrado","inseto","hematofago":
        print("pulga") 
    case "invertebrado","inseto","herbivoro":
        print("lagarta") 
    case "invertebrado","anelideo","hematofago":
        print("sanguessuga") 
    case "invertebrado","anelido","onivoro":
        print("minhoca")
    case _:
        print("input tidak valid")