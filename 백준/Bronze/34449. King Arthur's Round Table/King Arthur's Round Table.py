import sys
input = sys.stdin.readline

PI = 3.14159

d = float(input()) # 직경(피트)
w = float(input()) # 기사 당 공간(피트)
n = int(input()) # 기사 수

circumstance = PI * d
need = n * w
if circumstance >= need:
    print("YES")
else:
    print("NO")