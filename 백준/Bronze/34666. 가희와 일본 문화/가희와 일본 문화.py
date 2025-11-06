# bronzeIII_34666
import sys
input = sys.stdin.readline

q = int(input())

for _ in range(q):
    lv, a, b, c = map(int, input().split())

    if lv not in (1, 2):
        print("NO")
        continue

    if c < 50:
        print("NO")
        continue

    total_limit = 100 if lv == 1 else 90
    fail_limit = 18
    cond1 = 0 
    cond2 = 0 
    for score in (a, b):
        if score * 3 < total_limit:
            cond1 += 1
        if score <= fail_limit + 3:
            cond2 += 1
    if cond1 >= 2 or cond2 >= 1:
        print("YES")
    else:
        print("NO")
