import sys
input = sys.stdin.readline

n, q = map(int, input().split())

milk = {}
time = {}
for _ in range(q):
    c, keyword, h, m = input().strip().split()
    c = int(c)
    h, m = int(h), int(m)
    if keyword == 'START':
        milk[c] = [h, m]
    elif keyword == 'STOP':
        h0, m0 = milk[c]
        del milk[c]
        
        t = (h-h0)*60 + (m-m0)
        if c in time:
            time[c] += t
        else:
            time[c] = t

for i in range(1, n+1):
    h, m = time[i]//60, time[i]%60
    print(h, m)