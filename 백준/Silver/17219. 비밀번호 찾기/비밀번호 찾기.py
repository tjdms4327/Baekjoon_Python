import sys
input = sys.stdin.readline

n,m=map(int, input().split())
site={}
for _ in range(n):
    address, password=input().split()
    site[address]=password
for _ in range(m):
    s=input().strip()
    print(site[s])