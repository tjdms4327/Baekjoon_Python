import sys
input = sys.stdin.readline

n = int(input())

problems = []
for _ in range(9):
    P = list(map(int, input().split()))
    problems.append(max(P))

club = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']
cand_idx = problems.index(max(problems))
print(club[cand_idx])