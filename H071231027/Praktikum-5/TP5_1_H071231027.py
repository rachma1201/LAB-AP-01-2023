s1 = input("s1 = ")
s2 = input("s2 = ")
x = 0
s2 = s2[::-1]
s3 = ""
while x < len(s1) and x<len(s2):
    s3 += s1[x] + s2[x]
    x += 1
s3 += s1[x:]+s2[x:]
print(s3)
