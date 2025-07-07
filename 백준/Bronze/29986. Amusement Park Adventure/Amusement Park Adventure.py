ride, height=map(int, input().split())
rides=list(map(int, input().split()))

n=0
for i in rides:
    if height>=i:
        n+=1
print(n)