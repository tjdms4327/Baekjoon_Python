import sys
input = sys.stdin.readline

n = int(input())
matrix = [sum(list(map(int, input().split()))) for _ in range(n)]

print(sum(matrix))