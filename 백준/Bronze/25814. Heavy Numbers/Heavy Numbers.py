import sys
input = sys.stdin.readline

a, b = input().strip().split()
a_weigh = len(a) * sum(int(ch) for ch in a)
b_weigh = len(b) * sum(int(ch) for ch in b)

if a_weigh == b_weigh:
    print(0)
elif a_weigh > b_weigh:
    print(1)
else:
    print(2)