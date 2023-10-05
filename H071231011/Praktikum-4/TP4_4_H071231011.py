def CatAndMouse(CatA, CatB, MouseC):
    a = abs(CatA - MouseC)
    b = abs(CatB - MouseC)
    if a > b:
        return "Cat B"
    elif a < b:
        return"Cat A"
    elif a == b:
        return "Mouse C"

#case1
result1 = CatAndMouse(CatA= 20, CatB= 24, MouseC= 15)
print(result1)
    