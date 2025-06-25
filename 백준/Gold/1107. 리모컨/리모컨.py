n=int(input())
m=int(input())
if m!=0:
    broken=list(input().split())
else:
    broken=[]

min_clicks = abs(n - 100)
for target in range(1000000):
    for digit in str(target):
        if digit in broken:
            break
    else:
        min_clicks=min(min_clicks, len(str(target))+abs(target-n))
print(min_clicks)