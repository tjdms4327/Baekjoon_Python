# bronzeI_29732
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
s = [0] + list(input().strip())

result = s[:]
for i in range(1, n+1):
    if set(result) == {'R'}:
        break
    if s[i] == 'R':
        left = max(1, i - k)
        right = min(n, i + k)
        for x in range(left, right + 1):
            result[x] = 'R'

infected = result.count('R')
print("Yes" if infected <= m else "No")