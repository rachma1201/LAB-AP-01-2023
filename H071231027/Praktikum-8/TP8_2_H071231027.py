import re

ipv4_pattern = r"^((\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])$"
ipv6_pattern = r"^([\da-f]{0,4}:){7}[\da-f]{0,4}[\da-f]{0,4}$"

N = int(input())
check = []
for _ in range(N):
    input_line = input().strip()
    if len(input_line) <= 500:
        if re.match(ipv4_pattern,input_line):
            check.append("IPv4")
        elif re.match(ipv6_pattern,input_line):
            check.append("IPv6")
        else:
            check.append('Bukan IP Address')
    else:
        check.append("Bukan IP Address")
print()
for checkipv in check:
    print(checkipv, end="" '\n')
    
    













