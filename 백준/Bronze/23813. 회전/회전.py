import sys
input=sys.stdin.readline

n=list(map(int, input().strip()))
length=len(n)

sum_digit=sum(n)
tot=sum(sum_digit*(10**i) for i in range(length))
print(tot)