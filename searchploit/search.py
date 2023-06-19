import json
import os

print(os.system('searchsploit --nmap -t 127.0.0.1.xml -j > 127.0.0.1.json'))


# Opening JSON file
# f = open('127.0.0.1.json')
# data = (f)
# exploit = (data["RESULTS_EXPLOIT"])
# print(data)
# if exploit in ("", [], None, 0, False):
#     print ("No Exploit Found")
#     exploit = "No Exploit Found"
# else:
#     print(exploit)
#     exploit = exploit
# shellcode = (data["RESULTS_SHELLCODE"]["Path"])
# if shellcode in ("", [], None, 0, False):
#     print ("No shellcode Found")
#     shellcode = "No shellcode Found"
# else:
#     print(shellcode)
#     shellcode = shellcode
