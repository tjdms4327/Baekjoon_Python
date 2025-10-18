# bronzeII_8320
import sys
input = sys.stdin.readline

n = int(input())
count = 0 
for i in range(1 ,int(n**0.5)+1):
    count += (n//i - i + 1)
print(count)