import sys
input = sys.stdin.readline
n = int(input())
cnt = list(map(int, input().split()))

answer = -1
for x in range(n+1, -1, -1):
    if cnt.count(x) == x:
        answer = x
        break
    
print(answer)
        