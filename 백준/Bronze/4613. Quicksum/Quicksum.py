# bronzeII_4613
import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '#': break
    
    sum = 0
    for i in range(len(s)):
        ascii = (ord(s[i]) - ord('A') + 1 if s[i].isalpha() else 0)
        sum += (i + 1) * (ascii)
    print(sum)