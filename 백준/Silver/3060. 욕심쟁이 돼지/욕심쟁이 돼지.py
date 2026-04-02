import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    
    i = 1
    tot = sum(lst)
    while tot <= n:
        i += 1
        tot *= 4
    print(i)