# bronzeII_24937
import sys
input = sys.stdin.readline

s = 'SciComLove'

n = int(input())
x = n%10
print(s[x:]+s[:x])