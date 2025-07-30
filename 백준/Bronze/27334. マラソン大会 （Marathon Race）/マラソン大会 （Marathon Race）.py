n = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
ranks = []
for time in A:
    rank = sorted_A.index(time) + 1
    ranks.append(rank)

print(*ranks, sep='\n')
