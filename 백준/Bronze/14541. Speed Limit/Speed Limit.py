import sys
input = sys.stdin.readline

while True:  
    n = int(input())
    if n == -1: break
    
    distance = 0
    time = 0
    for _ in range(n):
        s, t = map(int, input().split())
        distance += s * (t - time)
        time = t
    print(f'{distance} miles')