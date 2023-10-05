def geserhuruf(n): 
    for i in range(len(n)):
        n = n[1:]+ n[0]
        print(n, end=" | ")
try:
    geserhuruf("#@!")
except TypeError:
    print("Terjadi error, N harus bertipe data string")