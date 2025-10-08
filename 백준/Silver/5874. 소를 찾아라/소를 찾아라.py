# silverIV_5874
import sys, bisect
input = sys.stdin.readline

s = input().strip()
n = len(s)
back = [i for i in range(n-1) if s[i] == '(' and s[i+1] == '(']
front = [i for i in range(n-1) if s[i] == ')' and s[i+1] == ')']

ans = 0
for b in back:
    count = len(front) - bisect.bisect_right(front, b)
    ans += count
print(ans)