i1 = input("Masukkan Input Pertama : ")
i2 = input("Masukkan Input Kedua : ")
i3 = input("Masukkan Input Ketiga : ")

match i1,i2,i3:
    case "vertebrado","ave","carnivoro":
        print("aguia")
    case "vertebrado","ave","onivoro":
        print("pombs")
    case "vertebrata","mamifero","onivoro":
        print("homem")
    case "vertebrata","mamifero","herbivoro":
        print("vaca")
    case "invertebrado","inseto","hematofago":
        print("pulga")
    case "invertebrado","inseto","herbivoro":
        print("lagarta")
    case "invertebrado","anelideo","hematofago":
        print("sanguessuga")
    case "invertebrado","anelideo","onivoro":
        print("minhoca") 
        