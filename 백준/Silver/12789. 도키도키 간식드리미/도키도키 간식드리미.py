# silverIII_12789
import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

stack = []
current = 1

for person in line:
    stack.append(person)
    while stack and stack[-1] == current:
        stack.pop()
        current += 1

if not stack or stack == sorted(stack, reverse=True):
    print('Nice')
else:
    print('Sad')