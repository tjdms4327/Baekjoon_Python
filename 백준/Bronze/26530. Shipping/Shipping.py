import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    tot=0
    t=int(input())
    byproducts=[list(input().split()) for _ in range(t)]
    for item in byproducts:
        tot += int(item[1]) * float(item[-1])
    print(f'${tot:.2f}')