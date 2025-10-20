from collections import deque

n = int(input())
s = deque(input().strip())

count = 0
while len(s) > 1:
    pair = s[0] + s[1] 
    if pair in ['XO', 'OX']:
        count += 1
        s.popleft()
    s.popleft()
print(count)
