import re
def cek_inputan(input_string):
    if len(input1) == 45:
        pola = r'^[a-zA-Z02468]{40}[13579\s]*$'
        if re.match(pola, input_string):
            print(True)
        else:
            print(False)
    else: 
        print("Panjang Karakter harus 45")
input1 = input()
cek_inputan(input1)
