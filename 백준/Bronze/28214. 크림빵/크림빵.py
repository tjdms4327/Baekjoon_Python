n, k, p = map(int, input().split())
bread = list(map(int, input().split()))



sell=0
for i in range(0, n*k, k):
    cream = sum(bread[i:i+k])
    if (k - cream) < p:
        sell+=1
print(sell)