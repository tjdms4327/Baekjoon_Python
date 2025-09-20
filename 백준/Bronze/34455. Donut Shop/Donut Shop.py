import sys
input = sys.stdin.readline

d = int(input()) # 도넛 수 (0 이상)
e = int(input())
for _ in range(e):
    event = input().strip()
    q = int(input())
    
    if event == '+':
        d += q
    else:
        d -= q
print(d)