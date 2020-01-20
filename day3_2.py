'''
Write regex for ipv4 and ipv6 address.
'''
import re
ip=input("Enter IP address")
if re.match(r"^(([2][0-4][0-9]|[2][5][0-5]|[0-1]?[0-9]?[0-9])[.]){3}([2][0-4][0-9]|[2][5][0-5]|[0-1]?[0-9]?[0-9])$",ip):
    print("It is IPv4 address")
elif re.match(r"([a-fA-F0-9]{4}:){7}[0-9a-fA-F]{4}",ip):
    print("It is IPv6 address")
else:
    print("Invalid address")
