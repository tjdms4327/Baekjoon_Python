n=int(input())
mirror=[]
for _ in range(n):
    mirror.append(input())
k=int(input())

if k==1:
    print(*mirror)
elif k==2:
    for m in mirror:
        print(m[::-1])
else:
    for i in range(n-1,-1,-1):
        for j in range(n):
            print(mirror[i][j], end='')
        print()