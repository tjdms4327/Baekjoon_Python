import sys
input = sys.stdin.readline

n, p = map(int, input().split())

result = str(pow(n, p))
for i in range(0, len(result), 70):
    print(result[i:i+70])