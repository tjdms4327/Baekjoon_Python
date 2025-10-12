# silverI_1711
import sys
input = sys.stdin.readline
from math import gcd
from collections import defaultdict

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    check = defaultdict(int)
    for j in range(n):
        if i == j:
            continue
		
        x, y = lst[i][0] - lst[j][0], lst[i][1] - lst[j][1] # 벡터
        val = gcd(x, y) # 기울기 방향만 남기기
        x, y = x // val, y // val 
        check[(x, y)] += 1 # 각 점마다 다른 점과의 기울기 저장
	
    for nx, ny in check:
        if check.get((-ny, nx)): # 내적 사용(두 벡터의 곱이 0이면 직각)
            answer += check[(nx, ny)] * check[(-ny, nx)]

print(answer)