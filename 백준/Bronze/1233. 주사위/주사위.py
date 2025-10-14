# bronzeII_1233
import sys
input = sys.stdin.readline
s1, s2, s3 = map(int, input().split())

sum_lst = [0]*(s1+s2+s3 + 1)
for a in range(1, s1+1):
    for b in range(1, s2+1):
        for c in range(1, s3+1):
            sum_lst[a+b+c] += 1
print(sum_lst.index(max(sum_lst)))