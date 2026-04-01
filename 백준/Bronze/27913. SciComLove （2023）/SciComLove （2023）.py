import sys
input = sys.stdin.readline

n, q = map(int, input().split())
Xs = [int(input())-1 for _ in range(q)] 

base = [1,0,0,1,0,0,1,0,0,0]
S = [base[i % 10] for i in range(n)]

count_upper = sum(S)
for x in Xs:
    if S[x] == 1:
        S[x] = 0
        count_upper -= 1
    else:
        S[x] = 1
        count_upper += 1
    print(count_upper)