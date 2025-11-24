import sys
input = sys.stdin.readline

n, q = map(int, input().split())

ballon = [False] * (n+1) # 1부터 시작

for _ in range(q):
    start, temp = map(int, input().split())
    
    for i in range(start, n+1, temp):
        if ballon[i] == True:
            continue
        else:
            ballon[i] = True
    
print(ballon.count(False) - 1)