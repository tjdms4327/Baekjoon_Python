t=int(input())
for _ in range(t):
    s=input().split()
    yoda=s[2:]+s[:2]
    print(*yoda, sep=' ')