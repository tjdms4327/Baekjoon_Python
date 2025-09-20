import sys
input = sys.stdin.readline

n = int(input()) # 위치
c = int(input()) # 칸 수
p = int(input()) # 칸 당 인원

if n <= c * p:
    print('yes')
else:
    print('no')