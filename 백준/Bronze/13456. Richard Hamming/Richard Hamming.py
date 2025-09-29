# bronzeIII_13456
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    length = int(input())
    v = list(input().split())
    u = list(input().split())
    
    count = 0
    for i in range(length):
        if v[i] != u[i]:
            count += 1
    print(count)