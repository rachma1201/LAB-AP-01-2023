a = float(input("Input a = "))
if a == 0:
    print("a tidak boleh sama dengan 0.")
else:
    # Menerima input b dan c
    b = float(input("input b = "))
    c = float(input("input c = "))

diskriminan = b**2 - 4*a*c
x1 = f"{(-b+(diskriminan**0.5))/(2*a):.2f}"
x2 = f"{(-b-(diskriminan**0.5))/(2*a):.2f}"

print (f"x1 = {x1}")
print (f"x2 = {x2}")




