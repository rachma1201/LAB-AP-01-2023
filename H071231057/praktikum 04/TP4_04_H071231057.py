def catAndMouse(catA, catB, mosC):
    # Menghitung jarak antara kucing A dan tikus
    distance_catA = abs(catA - mosC)
    
    # Menghitung jarak antara kucing B dan tikus
    distance_catB = abs(catB - mosC)
    
    # Memeriksa kondisi siapa yang lebih dulu mencapai tikus
    if distance_catA < distance_catB:
        return "Cat A"
    elif distance_catB < distance_catA:
        return "Cat B"
    else:
        return "Mouse C"

# Test Case 1
result1 = catAndMouse(catA=16, catB=24, mosC=15)
print(result1)  # Output: "Cat A"

# Test Case 2
result2 = catAndMouse(catA=20, catB=10, mosC=10)
print(result2)  # Output: "Mouse C"
