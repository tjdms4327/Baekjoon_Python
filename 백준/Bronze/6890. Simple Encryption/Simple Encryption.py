# bronzeII_6890
import sys
input = sys.stdin.readline

key_s = input().strip()
key = [ord(x) - ord('A') for x in key_s]

s = [x for x in input().strip() if x.isalpha()]
result = ''
for i in range(len(s)):
    x = (ord(s[i]) + key[i%len(key)] - ord('A')) % 26 + ord('A')
    result += chr(x)
print(result)