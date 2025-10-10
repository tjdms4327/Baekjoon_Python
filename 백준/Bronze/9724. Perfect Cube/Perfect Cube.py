# bronzeIII_9724
import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    a, b = map(int, input().split())
    count = 0
    for i in range(int(a**(1/3)) - 1, int(b**(1/3))+1):
        if a <= i**3 <= b:
            count += 1
    print(f'Case #{case}: {count}')