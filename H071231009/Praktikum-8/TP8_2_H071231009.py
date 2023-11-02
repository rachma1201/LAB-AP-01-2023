import re

jumlah_inputan = int(input())

list_karakter = []
for i in range(jumlah_inputan):
    karakter = input()
    if len(karakter) <= 500:
        list_karakter.append(karakter)
    else:
        print("Bukan IP Address")

def cek_ip(teks):
    cekIpv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    cekIpv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    for karakter in teks:
        if re.match(cekIpv4, karakter):
            print("IPv4")
        elif re.match(cekIpv6, karakter):
            print("IPv6")
        else:
            print("Bukan IP Address")

cek_ip(list_karakter) 