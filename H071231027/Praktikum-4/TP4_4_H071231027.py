def minimum(catA, catB, mosC):
    try:  
        catA_mosC = (catA - mosC)
        if catA_mosC < 0:
            catA_mosC = -(catA_mosC)

        catB_mosC = (catB - mosC)
        if catB_mosC < 0:
            catB_mosC = -(catB_mosC)

        if catA_mosC < catB_mosC:
            print("catA")
        elif catB_mosC < catA_mosC:
            print("catB")
        else:
            print("mosC")
    except:
        print("\nType Error")

print("Test 1")
minimum(catA= 16, catB= 24, mosC= 15)

print("\nTest Case 2")
minimum(catA= 20, catB= 20, mosC= 10)


