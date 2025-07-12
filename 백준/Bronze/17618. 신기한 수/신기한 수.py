import sys
input=sys.stdin.readline

def sum_digit(i):
    s=0
    while i:
        s+=(i%10)
        i//=10
    return s
    
n=int(input().strip())
cnt=0
for i in range(1, n+1):
    if i<10: cnt+=1
    else:
        if i%sum_digit(i)==0: cnt+=1
print(cnt)