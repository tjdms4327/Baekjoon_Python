# bronzeIII_15429
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    g, *id = map(int, input().split())
    
    for i in range(1, g):
        if id[i-1] + 1 != id[i]:
            print(i+1)
            break