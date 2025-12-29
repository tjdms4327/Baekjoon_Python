import sys
input = sys.stdin.readline

n, m = map(int, input().split())

reservation = {}
for _ in range(m):
    k, s, e = map(int, input().split())
    
    if k not in reservation:
        reservation[k] = (s, e)
        print('YES')
    else:
        past_s, past_e = reservation[k]
        if past_e <= s:
            reservation[k] = (s, e)
            print('YES')
        else:
            print('NO')
        