import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    a, b, k = map(int, input().split())
    
    count = 0
    for x in range(a):
        for y in range(b):
            result = int(bin(x & y)[2:], 2)
            if result < k:
                count += 1
    print(f'Case #{case}: {count}')