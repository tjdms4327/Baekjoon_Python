# bronzeIII_26741
import sys
input = sys.stdin.readline

y, x = map(int, input().split())

cow = (x - 2*y) // 2
print(y - cow, cow)