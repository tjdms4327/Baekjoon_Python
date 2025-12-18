import sys, math
input = sys.stdin.readline

n = int(input())
s = input().strip()

if len(set(s))==1:
    print('Yes')
    sys.exit()

divisor = set()
for i in range(2, math.isqrt(n)+1):
    if n%i==0:
        divisor.add(i)
        divisor.add(n//i)
        
for i in divisor:
    slice = s[:i]
    if slice*(n//i) == s:
        print('Yes')
        sys.exit()
print('No')