import sys
input=sys.stdin.readline

n=int(input())
if n>=(-1)*2**15 and n<=2**15-1:
    print('short')
elif n>=(-1)*2**31 and n<=2**31-1:
    print('int')
else:
    print('long long')