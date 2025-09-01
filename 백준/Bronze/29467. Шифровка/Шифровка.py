import sys
input = sys.stdin.readline

s = input().strip()
best = ""
for i in range(len(s)-1, -1, -1):
    if s[i:] > best:
        best = s[i:]
print(best)