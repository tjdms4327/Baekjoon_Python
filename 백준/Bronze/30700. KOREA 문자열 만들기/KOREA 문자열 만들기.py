# bronzeII_30700
import sys, math
input = sys.stdin.readline

s = input().strip()
result = []
for i in s:
    if ((not result) or (result and result[-1] == 'A')) and i == 'K':
        result.append(i)
    elif result and result[-1]=='K' and i=='O':
        result.append(i)
    elif result and result[-1]=='O' and i=='R':
        result.append(i)
    elif result and result[-1]=='R' and i=='E':
        result.append(i)
    elif result and result[-1]=='E' and i=='A':
        result.append(i)
print(len(result))