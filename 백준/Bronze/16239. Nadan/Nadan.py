import sys
input = sys.stdin.readline

k = int(input()) # 총 금액
n = int(input()) # 프로젝트 수

result = list(range(1, n))
result.append(k - sum(result))
print(*result, sep = '\n')