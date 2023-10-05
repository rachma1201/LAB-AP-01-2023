def catAndMouse(catA, catB, mousC):
    jarak_A_ke_tikus = abs(catA - mousC)
    jarak_B_ke_tikus = abs(catB - mousC)

    if jarak_A_ke_tikus < jarak_B_ke_tikus:
        return "Cat A"
    elif jarak_A_ke_tikus > jarak_B_ke_tikus:
        return "Cat B"
    else:
        return "Mouse C"
    
catA = int(input())
catB = int(input())
mousC = int(input())
print(catAndMouse(catA, catB, mousC))