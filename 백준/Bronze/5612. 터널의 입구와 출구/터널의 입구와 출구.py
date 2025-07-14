n=int(input())
m=int(input())

max_m=m
for i in range(n):
    enter, out=map(int, input().split())
    m+=enter ; m-=out
    if m<0: max_m=0; break
    if max_m<m: max_m=m
print(max_m)