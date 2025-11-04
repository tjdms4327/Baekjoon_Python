# silverIII_17952
import sys
input = sys.stdin.readline

n = int(input())

stack = []
total = 0
for _ in range(n):
    s = list(map(int, input().split()))
    if s[0] == 1:
        score, t = s[1], s[2]
        t -= 1
        if t == 0:
            total += score
        else:
            stack.append([score, t])
    else:
        if stack:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                total += stack[-1][0]
                stack.pop()

print(total) 