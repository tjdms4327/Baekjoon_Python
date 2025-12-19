import sys
input = sys.stdin.readline

n = int(input())
separater = list(input().strip().split())
m = int(input())
n_separate = list(input().strip().split())
separater.extend(n_separate)
separater.append(' ')
k = int(input())
merger = list(input().strip().split())

n = int(input())
s = list(input().strip())

result = []
cur = ''
for ch in s:
    if ch in merger:
        cur += ch
    elif ch in separater:
        if cur:
            result.append(cur)
        cur = ''
    else:
        cur += ch
if cur:
    result.append(cur)
print(*result, sep='\n')