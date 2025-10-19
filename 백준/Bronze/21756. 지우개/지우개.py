# bronzeII_21756
import sys
input = sys.stdin.readline

n = int(input())
lst = list(range(1, n+1))

while len(lst) > 1:
    lst = lst[1::2]
print(*lst)