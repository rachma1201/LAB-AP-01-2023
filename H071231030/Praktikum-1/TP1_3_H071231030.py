#Nomor 3
a = float(input("nilai a ="))
b = float(input("nilai b ="))
c = float(input("nilai c ="))

diskriminan = b**2 - 4*a*c
x1 = (-b+(diskriminan)**(0.5))/2*a
x2 = (-b-(diskriminan)**(0.5))/2*a

print (f"nilai x1 = {x1:.2f}")
print (f"nilai x2 = {x2:.2f}")