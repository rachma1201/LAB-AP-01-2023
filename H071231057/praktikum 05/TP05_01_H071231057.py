# def string(s1=input(""),s2=input("")) :
#     s3 = s1 + s2   
#     if len(s3) <= 6 :
#       print(s1[0] + s2[-1] + s1[1] + s2[-2] + s1[2] + s2[-3])
      
    
#     elif len(s3) >= 6 :
#      print(s1[0] + s2[-1] + s1[1] + s2[-2] + s1[2] + s2[-3] + s1[-3:] + s2[0])
     
   


   
# hasil = string()






# mixed = string(s1=input(""),s2=input(""))
# print("HASIL MIXED ADALAH :", mixed)


# s1 = input("")
# s2 = input("")[::-1]
# result=""
    

   
# i = 0
# if i < len(s1) and i < len(s2):
#       result += s1[i] + s2[i]
#       i += 1
#       result += s1[i:] + s2[i:-2]

    
# print("HASILNYA ADALAH:", result)

s1 = input("")
s2 = input("")[::-1]
s3 = ""
i = 0
while i < len(s1) and i < len(s2):
    s3 += s1[i] + s2[i]
    i += 1
s3 += s1[i:] + s2[i:]
print("HASILNYA ADALAH: ",s3)