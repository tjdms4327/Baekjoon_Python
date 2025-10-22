# bronzeII_23738
import sys
input = sys.stdin.readline

mapping = {'B':'v', 'E':'ye', 'H':'n', 'P':'r', 'C':'s', 'Y':'u', 'X':'h'}

s = input().strip()
result = ''
for ch in s:
    if ch in mapping:
        result += mapping[ch]
    else:
        result += ch.lower()
print(result)