from math import ceil

n=int(input())
file_size=list(map(int, input().split()))
cluster=int(input())

cluster_size=0
for i in file_size:
    cluster_size+=ceil(i/cluster)*cluster
print(cluster_size)