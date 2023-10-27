# def header() :
#     '''FUNGSI HEADER'''
# import os
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS' : ^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG' : ^40}")
# print(f"{'-'*40 : ^40}")


# def inputan_anagram() :
#     '''INI ADALAH INPUTAN KATA ANAGRAM'''
#     KATA_1 = input("MASUKKAN KATA PERTAMA : ")
#     KATA_2 = input("MASUKKAN KATA KEDUA : ")
#     return KATA_1,KATA_2

# while True :
#     header()
#     KATA_1,KATA_2 = inputan_anagram()

#     if len(KATA_1) == len(KATA_2) :
#         print((True))
#         break
#     elif len(KATA_1) != len(KATA_2) :
#         print(False)
#         break

# def anagram(st1, st2) :
#     lower = st1.lower() and st2.lower()
#     replace_ = lower.replace()

# string1 = ("I am Lord Voldemort")
# string2 = ("Tom Marvolo Riddle")
# lower1 = string1.lower() 
# lower2 = string2.lower()
# replace1 = lower1.replace(" ", "") 
# replace2 = lower2.replace(" ","")
# kata1 = list(replace1)
# kata2 = list(replace2)
# kata1.sort()
# kata2.sort()

# if kata1 == kata2 :
#     print(True)
# else :
#     print(False)
    
# def header() :
#     '''FUNGSI HEADER'''
# import os
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS' : ^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG' : ^40}")
# print(f"{'-'*40 : ^40}")

# def inputan_anagram() :
#   '''[INPUTAN ANAGRAM]'''
    # I am Lord Voldemort
    # Tom Marvolo Riddle
st_1 = input("MASUKKAN KATA 1 :").replace(" ", "").lower()  # I am Lord Voldemort
st_2 = input("MASUKKAN KATA 2 :").replace(" ", "").lower() # Tom Marvolo Riddle
a = sorted(st_1)
b = sorted(st_2)
# print(st_1)
# print(st_2)

if len(a) == len(b) :
     
 if a == b : 
    print("True")

else :
     print("NOT TRUE")
    


