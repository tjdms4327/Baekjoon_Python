import sys
input = sys.stdin.readline

n = int(input())

pocketmon = {}
for _ in range(n):
    name = input().strip()
    k, m = map(int, input().split())
    
    count = 0
    while k <= m:
        count += 1
        m = m - k + 2
    pocketmon[name] = count
    

tot = sum(pocketmon.values())
print(tot)

sorted_pocketmon = sorted(pocketmon.items(), key=lambda x: -x[1])
print(sorted_pocketmon[0][0])