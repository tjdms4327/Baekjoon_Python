import sys
input=sys.stdin.readline

l=int(input())
n=int(input())
t=float(input())
for _ in range(n):
    f, b=map(float, input().split())
    if (l/f + l/b) < t:
        print('HOPE')
        sys.stdin.read() # 남은 입력 모두 읽기
        exit(0)
print('DOOMED')
