import sys
input=sys.stdin.readline

n=int(input())
meet=[tuple(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1],x[0]))

time=0
count=0
for start, end in meet:
    if start>=time:
        count+=1
        time=end
print(count)