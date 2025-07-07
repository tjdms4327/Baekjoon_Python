t,x=map(int, input().split())
n=int(input())
yn='YES'
for _ in range(n):
    ki=int(input())
    ai=list(map(int, input().split()))
    if x not in ai:
        yn='NO'
        break
print(yn)