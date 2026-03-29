import sys
input = sys.stdin.readline

target = input().strip()
n = int(input())

cnt = 0
for _ in range(n):
    s = input().strip()
    s += s
    
    if target in s:
        cnt += 1
        
print(cnt)