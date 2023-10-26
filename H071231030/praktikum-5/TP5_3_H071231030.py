kata1 = input("Masukkan Kata Pertama : ").replace(" ", "").lower()
kata2 = input("Masukkan Kata Kedua : ").replace(" ", "").lower()
error = 0

for i in  kata1:
    status1 = kata1.count(i)
    status2 = kata2.count(i)
    if status1 != status2:
        error += 1

if error == 0:
    print ("True")
else:
    print ("False")