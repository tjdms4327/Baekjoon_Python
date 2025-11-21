import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    a, m = map(int, input().split())
    
    cost = (a * m * 1056) // 600000
    print(cost)