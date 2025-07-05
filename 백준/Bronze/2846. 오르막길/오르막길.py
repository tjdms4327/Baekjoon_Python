n=int(input())
roads=list(map(int, input().split()))

height=[0]
down, up=roads[0], roads[0]
for i in range(1,len(roads)):
    if roads[i]<=roads[i-1]:
        height.append(up-down)
        down, up=roads[i], roads[i]
    elif roads[i]>roads[i-1]:
        up=roads[i]

height.append(up-down)
print(max(height))