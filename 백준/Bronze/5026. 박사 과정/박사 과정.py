import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    problem=input().strip()
    if problem=='P=NP':
        print('skipped')
    else:
        nums=[int(i) for i in problem.split('+')]
        print(sum(nums))