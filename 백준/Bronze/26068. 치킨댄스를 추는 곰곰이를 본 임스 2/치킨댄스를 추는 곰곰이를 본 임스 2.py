n=int(input())

count=0
for _ in range(n):
    day=input()
    d_day=int(day[2:])
    if d_day<=90:
        count+=1
print(count)