import sys
input = sys.stdin.readline

q = int(input())


def is_power_2(n):
    return int(n > 0 and (n & (n-1)) == 0)
    
for _ in range(q):
    a = int(input())
    print(is_power_2(a))