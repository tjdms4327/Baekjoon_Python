import sys
input = sys.stdin.readline

from datetime import datetime
fmt  = "%Y-%m-%d"

now = datetime.strptime(input().strip(), fmt)
n = int(input())
count = sum(1 for _ in range(n) 
           if now <= datetime.strptime(input().strip(), fmt))
print(count)