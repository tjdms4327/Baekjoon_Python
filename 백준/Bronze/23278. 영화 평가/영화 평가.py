# bronzeI_23278
import sys
input = sys.stdin.readline

n, l, h = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort()
new_lst = scores[l:-h] if h!=0 else scores[l:]
if not new_lst:
    print(0)
else:
    print(sum(new_lst) / len(new_lst))