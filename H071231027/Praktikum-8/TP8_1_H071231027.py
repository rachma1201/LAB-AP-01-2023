import re

input_string = input("Masukkan string: ")
pattern = r'^[a-zA-Z0-9]{40}[13579\s]{5}$'
if re.match(pattern, input_string) and len(input_string) == 45:
    print(True)
else:
    print(False)




















