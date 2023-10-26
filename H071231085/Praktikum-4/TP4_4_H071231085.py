def catAndMouse(catA, catB, MouseC):
    a = (catA - MouseC)
    if a < 0 :
        a = -(catA - MouseC)
    b = (catB - MouseC)
    if b < 0 :
        b = -(catB - MouseC)
    if a > b :
        print("cat B")
    elif a < b :
        print("cat A")
    else:
        print("Mouse C")

catAndMouse(catA = 16, catB =24, MouseC = 15)