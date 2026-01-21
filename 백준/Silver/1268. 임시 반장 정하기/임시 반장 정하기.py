import sys
input = sys.stdin.readline

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

cand = [0]*(n)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if any(students[i][k] == students[j][k] for k in range(5)):
            cand[i] += 1
print(cand.index(max(cand)) + 1)