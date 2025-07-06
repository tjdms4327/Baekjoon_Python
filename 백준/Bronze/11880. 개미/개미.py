import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    lens=list(map(int, input().split()))
    lens.sort()
    h=lens[0]+lens[1]
    print(h**2+lens[-1]**2)