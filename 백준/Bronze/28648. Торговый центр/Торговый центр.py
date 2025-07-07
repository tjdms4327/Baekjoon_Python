n=int(input())
busmin=201
for _ in range(n):
    ti, li=map(int, input().split())
    if ti+li<busmin:
        busmin=ti+li
print(busmin)