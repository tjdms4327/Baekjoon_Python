import sys
input = sys.stdin.readline

k, n = map(int, input().split())
s = input().strip()

result = ''
for x in s:
    if 'A' <= x <= 'Z':
        result += chr((ord(x)-ord('A')+k)%26 + ord('A'))
    elif 'a' <= x <= 'z':
        result += chr((ord(x)-ord('a')+k)%26 + ord('a'))
    else:
        result += x
print(result)