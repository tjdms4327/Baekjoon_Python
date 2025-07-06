n=int(input())
k=int(input())

in_need=min(n, k+60)
over_need=max(0, n-k-60)
print(in_need*1500+over_need*3000)