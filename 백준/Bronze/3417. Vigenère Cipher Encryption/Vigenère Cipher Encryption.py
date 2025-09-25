# bronzeII_3417
import sys
input = sys.stdin.readline

while True:
    key_s = input().strip()
    if key_s == '0': break

    key = [ord(x) - ord('A') + 1 for x in key_s]
    s = input().strip()
    
    result = []
    for i in range(len(s)):
        x = (ord(s[i]) + key[i%len(key)] - ord('A')) % 26 + ord('A')
        result.append(chr(x))
    print(''.join(result))