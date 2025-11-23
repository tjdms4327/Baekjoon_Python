import sys
input = sys.stdin.readline

w, p = map(int, input().split())
parts = [0] + list(map(int, input().split())) + [w]

ans = set()
for i in range(len(parts)):
    for j in range(i+1, len(parts)):
        ans.add(parts[j] - parts[i])
print(*sorted(ans))