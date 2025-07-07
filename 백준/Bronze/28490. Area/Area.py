n=int(input())

max=0
for _ in range(n):
    h, w=map(int, input().split())
    area=h*w
    if area>max:
        max=area
print(max)