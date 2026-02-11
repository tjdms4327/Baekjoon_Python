import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    call = []
    for _ in range(n):
        _, _, start, duration = map(int, input().split())
        end = start + duration
        call.append((start, end))
    
    for _ in range(m):
        start, duration = map(int, input().split())
        end = start + duration
        
        count = 0
        for s, e in call:
            if s < end and start < e:
                count += 1
        print(count)
