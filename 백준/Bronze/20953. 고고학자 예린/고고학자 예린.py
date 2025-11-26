import sys
input = sys.stdin.readline

def dolmen(a, b):
    x = a+b
    return x*(x*(x-1)//2)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(dolmen(a, b))
    