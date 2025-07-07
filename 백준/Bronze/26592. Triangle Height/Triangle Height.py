import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    area, base=map(float, input().split())
    print(f'The height of the triangle is {2*area/base:.2f} units')