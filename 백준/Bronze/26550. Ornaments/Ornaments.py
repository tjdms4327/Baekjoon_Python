import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    h = int(input())
    print(h*(h+1)*(h+2)//6)