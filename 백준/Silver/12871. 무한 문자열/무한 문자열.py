import sys, math
input = sys.stdin.readline

s = input().strip()
t = input().strip()

lcm = math.lcm(len(s), len(t))

new_s = s * (lcm // len(s))
new_t = t * (lcm // len(t))

if new_s == new_t:
    print(1)
else:
    print(0)