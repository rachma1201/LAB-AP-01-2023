kata1, kata2 = input("Input Pertama : "), input("Input Kedua : ")
kata1, kata2 = kata1.replace(" ", "").lower(), kata2.replace(" ", "").lower()
list1, list2 = [], []
for i in kata1:
    x, y = kata1.count(i), kata2.count(i)
    list1.append(x)
    list2.append(y)
if len(kata1) == len(kata2):
    if list1 == list2:
        print("True")
    else:
        print("False")
else:
    print("False")