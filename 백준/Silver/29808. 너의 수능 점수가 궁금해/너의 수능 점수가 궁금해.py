import sys
input = sys.stdin.readline

s = int(input())
if s % 4763 != 0:
    print(0)
    sys.exit()
    
T = s // 4763
cases = [
    (508, 212),
    (508, 305),
    (108, 212),
    (108, 305)
]

ans = set()
for x, y in cases:
    for a in range(201):
        rem = T - x * a
        if rem < 0:
            continue
        if rem % y != 0:
            continue
        b = rem // y
        if 0 <= b <= 200:
            ans.add((a, b))

print(len(ans))
for a, b in sorted(ans):
    print(a, b)