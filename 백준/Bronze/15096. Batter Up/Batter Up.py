import sys
input = sys.stdin.readline

n = int(input())
result = list(map(int, input().split()))

result_pos = [x for x in result if x >= 0]
print(sum(result_pos) / len(result_pos))