# bronzeIV_34722
import sys
input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    boj, codeforces, atcoder, icpc = map(int, input().split())
    
    if boj >= 1000 or codeforces >=1600 \
        or atcoder >= 1500 or (icpc != -1 and icpc <= 30):
            count += 1
print(count)