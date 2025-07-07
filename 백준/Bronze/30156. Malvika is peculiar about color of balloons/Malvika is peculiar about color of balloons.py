t=int(input())
for _ in range(t):
    ballon=input()
    a=ballon.count('a')
    print(min(a, len(ballon)-a))