n=int(input())
seat=[0]
rest=0
for _ in range(n):
    a, b=map(int, input().split())
    rest+=(b-a)
    seat.append(rest)
print(max(seat))