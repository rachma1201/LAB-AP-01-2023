def CatAndMouse(CatA, CatB, MouseC):
    a = ((CatA - MouseC)**2)**0.5 #bentuk lain mencari jarak, ada bentuk simple nya yaitu abs
    b = ((CatB - MouseC)**2)**0.5 
    if a > b:
        print("Cat B")
    elif a < b:
        print("Cat A")
    elif a == b:
        print("Mouse C")

CatAndMouse(CatA=-20, CatB=41, MouseC=12)