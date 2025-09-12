import sys
input = sys.stdin.readline

n = int(input())
p = int(input())  # 지수 1~3
potentials = list(map(int, input().split()))
pos = [i for i in potentials if i > 0]

if p == 1:
    print(sum(pos))
elif p == 2:
    print(sum(i**2 for i in potentials))
else: # p==3
    print(sum(i**3 for i in pos))