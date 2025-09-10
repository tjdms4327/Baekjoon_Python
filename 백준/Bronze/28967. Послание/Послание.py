import sys
input = sys.stdin.readline

c = input().strip()
s = input().strip()

count = 0
i = 0
for ch in s:
    if ch == c[i]:
        i += 1
    if i == len(c):
        count += 1
        i = 0
print(count)