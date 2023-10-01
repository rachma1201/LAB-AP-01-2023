print("Bentuk Persamaan Kuadrat  : ax**2+bx+c")
a = float(input("input a : "))
b = float(input("input b : "))
c = float(input("input c : "))
if a == 0:
    print("nilai a tidak boleh nol")
else:
    x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
print(f"x1 : {x1:.2f}")
print(f"x2 : {x2:.2f}")
