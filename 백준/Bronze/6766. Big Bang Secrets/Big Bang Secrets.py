# bronzeII_6766
import sys
input = sys.stdin.readline

k = int(input())
s = input().strip()

result = ''
for i in range(len(s)):
    push = 3 * (i+1) + k
    x = (ord(s[i]) - push - ord('A')) % 26 + ord('A')
    result += chr(x)
print(result)