import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())

P = [idx for idx in range(n) if s[idx]=='P']
C = [idx for idx in range(n) if s[idx]=='C']

for i in range(min(len(P), len(C))):
    s[P[i]], s[C[i]] = s[C[i]], s[P[i]]
    
print(''.join(s))