import sys
input = sys.stdin.readline

n = int(input().strip())

visited = set()
while n != 1 and n not in visited:
    visited.add(n)
    n = sum(int(d)**2 for d in str(n))

if n == 1:
    print("HAPPY")
else:
    print("UNHAPPY")