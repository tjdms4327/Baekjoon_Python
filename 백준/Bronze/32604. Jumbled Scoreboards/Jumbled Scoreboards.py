n=int(input())
AB=[list(map(int, input().split())) for _ in range(n)]

default='yes'
for i in range(n-1):
    if AB[i][0]>AB[i+1][0] or AB[i][1]>AB[i+1][1]:
        default='no'
        break
print(default)