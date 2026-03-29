import sys
input = sys.stdin.readline

def cal(n):
    cnt = 0
    
    while n != "6174":
        max_num = int(''.join(sorted(n, reverse=True)))
        min_num = int(''.join(sorted(n)))
        
        n = str(max_num - min_num).zfill(4)
        cnt += 1
    
    return cnt

t = int(input())
for _ in range(t):
    n = input().strip()
    print(cal(n))