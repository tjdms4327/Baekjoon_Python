import sys
input=sys.stdin.readline
    
n=int(input().strip())
cnt=0
for i in range(1, n+1):
    if i<10: cnt+=1
    else:
        i_digit=list(map(int, str(i)))
        if i%sum(i_digit)==0: cnt+=1
print(cnt)