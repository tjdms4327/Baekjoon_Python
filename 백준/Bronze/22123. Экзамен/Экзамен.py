# bronzeIII_22123.py
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s, f, k = input().strip().split()
    S = list(map(int, s.split(":")))
    F = list(map(int, f.split(":")))
    k = int(k)
    
    S_min = S[0]*60 + S[1] + S[2]/60
    F_min = F[0]*60 + F[1] + F[2]/60
    time = F_min - S_min
    if time <= 0:
        time += 24*60
    
    if time >= k:
        print('Perfect')
    elif time + 60 >= k:
        print('Test')
    else:
        print('Fail')