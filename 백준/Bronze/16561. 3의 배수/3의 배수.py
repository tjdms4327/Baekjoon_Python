# bronzeII_16561
import sys
input = sys.stdin.readline

n = int(input())

divided_n = n //3
count = (divided_n - 1) * (divided_n - 2) // 2
print(count)