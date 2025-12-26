import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    score = {i: [0, 0] for i in range(1, n+1)}
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        score[a][0] += p
        score[a][1] += q
        score[b][0] += q
        score[b][1] += p
    
    result = []
    for i in range(1, n+1):
        s, a = score[i]
        if s == 0 and a == 0:
            w = 0
        else:
            w = int((s**2) / (s**2 + a**2) * 1000)
        result.append(w)

    print(max(result))
    print(min(result))
