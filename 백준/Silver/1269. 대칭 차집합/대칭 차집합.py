n,m=map(int, input().split())

a=set(input().split())
b=set(input().split())
sym_diff=list(a^b)
print(len(sym_diff))




