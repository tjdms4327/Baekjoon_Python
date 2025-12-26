import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, r, s = map(int, input().split())
    
    count = 1
    i = 1
    while s!=l and s!=r:
        if i%2==1:
            s += i
        else:
            s -= i
        i += 1
        count += 1
    print(count)