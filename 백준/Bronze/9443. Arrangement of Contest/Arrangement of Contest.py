import sys
input = sys.stdin.readline

n = int(input())

abc = set()
for i in range(n):
    s = input().strip()
    abc.add(s[0])

first_letters = sorted(abc)
count = 0
for i, c in enumerate(first_letters):
    if ord(c) - ord('A') != i: 
        break
    count += 1
print(count)