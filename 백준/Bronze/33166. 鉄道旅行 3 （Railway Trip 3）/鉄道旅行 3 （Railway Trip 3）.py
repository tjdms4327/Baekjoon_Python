import sys
input=sys.stdin.readline

p,q=map(int, input().strip().split())
a,b=map(int, input().strip().split())
if q<=p: print(q*a) # 할인거리 p보다 총이동거리 q가 작은 경우
else: print(p*a+(q-p)*b)