s1, s2, s3 = input("S1 = "), input("S2 = "), ""
s2, p = ''.join(reversed(s2)), min(len(s1), len(s2))
for i in range (p):
    s3 += s1[i] + s2[i]
s3 += s1[p:] + s2[p:]
print(f'Hasil Mixed = "{s3}"')