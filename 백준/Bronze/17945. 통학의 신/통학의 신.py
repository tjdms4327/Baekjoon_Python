import sys
input=sys.stdin.readline

a,b=map(int, input().split())



from math import sqrt
# x = (-a +- root(a**2-1*b)) //1
minus_a=(-1)*a
in_root=a**2-b
if in_root==0: # 중근
    print(minus_a)
elif in_root>0: # 두 개의 해
    print(minus_a-int(sqrt(in_root)), minus_a+int(sqrt(in_root)))
# 이 방정식의 근은 항상 정수이므로 허수근은 없다.
