import sys
input=sys.stdin.readline

n=int(input())
births=[list(input().split()) for _ in range(n)]
births.sort(key=lambda x:((int(x[-1]), int(x[-2]), int(x[-3]))))
print(births[-1][0])
print(births[0][0])
