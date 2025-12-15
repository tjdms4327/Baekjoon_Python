import sys
input = sys.stdin.readline

x = int(input())
m = int(input())

for n in range(1, m):
    if x*n%m==1:
        print(n)
        sys.exit()
print('No such integer exists.')