import sys
input=sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
    name, korean, english, math = input().strip().split()
    lst.append([name, int(korean), int(english), int(math)])
lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in lst:
    print(i[0])