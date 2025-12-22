import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    n, m = map(int, input().split())
    sejun = list(map(int, input().split()))
    sebi = list(map(int, input().split()))
    
    if max(sejun) >= max(sebi):
        print('S')
    else:
        print('B')