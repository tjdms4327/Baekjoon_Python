import sys
input=sys.stdin.readline

now=list(map(int, input().split(':')))
want=list(map(int, input().split(':')))
remain=[want[i]-now[i] for i in range(3)]

if remain[-1]<0:
    remain[-1]+=60
    remain[1]-=1
if remain[1]<0:
    remain[1]+=60
    remain[0]-=1
if remain[0]<0:
    remain[0]+=24
print(f'{remain[0]:02d}:{remain[1]:02d}:{remain[-1]:02d}')