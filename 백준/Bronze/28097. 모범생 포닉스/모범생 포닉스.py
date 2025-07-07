n=int(input())
t=list(map(int,input().split()))

s=(n-1)*8+sum(t)
print(s//24, s%24)