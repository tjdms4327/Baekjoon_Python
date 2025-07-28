n=int(input())
s=list(input().strip().split())

result=[i+'DORO' for i in s]
print(*result, sep=' ')