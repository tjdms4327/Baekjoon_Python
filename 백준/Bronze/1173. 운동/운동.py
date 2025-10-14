# bronzeII_1173
import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
    exit()
    
pulse = m
time = 0
exercise = 0 
while exercise < N:
    if (pulse + T) <= M:
        pulse += T
        exercise += 1
    else:
        pulse -= R
    time += 1
    pulse = max(m, pulse)
print(time)