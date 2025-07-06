import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    candy, p=map(int, input().split())
    print(f'You get {candy//p} piece(s) and your dad gets {candy%p} piece(s).')