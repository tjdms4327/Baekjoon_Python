# bronzeII_33869
import sys
input = sys.stdin.readline

w = input().strip()
s = input().strip()

key = ""
for ch in w:
    if ch not in key:
        key += ch
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for ch in alphabet:
    if ch not in key:
        key += ch
        
encrypt = {}
for i in range(26):
    encrypt[alphabet[i]] = key[i]

encode = ''.join(encrypt[ch] for ch in s)
print(encode)