import sys
input = sys.stdin.readline

k = int(input())
for case in range(1, k+1):
    n, m, T = map(int, input().split())
    
    contribute = [[] for _ in range(n + 1)]
    for _ in range(m):
        i, t, d = input().strip().split()
        i = int(i)
        t = int(t)
        d = float(d)
        if 0 <= T-t < 1000:
            contribute[i].append(d)
        
    votes = [input().strip() for _ in range(n)]
    vote_yes = 0.0
    vote_no = 0.0
    for i in range(1, n+1):
        if votes[i - 1] == 'Y':
            vote_yes += 1.0
        else:
            D = sum(contribute[i])
            vote_no += 1.0 / (1 + (D / 10000.0))
        
    print(f'Data Set {case}:')
    print(f"{vote_yes:.2f} {vote_no:.2f}\n")