n=int(input())
a=list(map(int, input().split()))
a=sorted(set(a))

print(*a, sep='\n')