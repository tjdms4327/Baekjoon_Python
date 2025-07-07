s=[]

n=int(input())
for _ in range(n):
    period=input()
    if period[-1]!='.':
        period+='.'
    s.append(period)
print(*s, sep='\n')