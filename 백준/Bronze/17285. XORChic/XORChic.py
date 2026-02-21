import sys
input = sys.stdin.readline

t = input().strip()

key = ord(t[0]) ^ ord('C')
result = ''
for x in t:
    result += chr(key ^ ord(x))
print(result)