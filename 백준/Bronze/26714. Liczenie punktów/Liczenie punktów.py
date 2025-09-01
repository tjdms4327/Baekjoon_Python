import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

cnt = 0
for i in range(0, n, n//10):
    block = s[i : i + n//10]
    if all(ch == 'T' for ch in block):
        cnt += 1
print(cnt)