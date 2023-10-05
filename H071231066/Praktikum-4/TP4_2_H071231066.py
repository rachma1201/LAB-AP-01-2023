def palindrom(x : str) -> str:
    x = x.lower()
    if x == x[::-1]:
        print("Palindrom")
    else:
        print("Bukan Palindrom")
palindrom("Radar")