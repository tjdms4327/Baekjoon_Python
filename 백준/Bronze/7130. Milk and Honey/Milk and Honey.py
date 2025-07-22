m, h=map(int, input().split())
n=int(input())

tot=0
for _ in range(n):
    c, b=map(int, input().split())
    tot+=max(m*c, b*h)
print(tot)