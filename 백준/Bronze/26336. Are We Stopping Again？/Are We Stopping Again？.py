import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    mile, fuel, eat = map(int, input().split())
    
    print(mile, fuel, eat)
    mile -= 1
    print(mile//fuel + mile//eat - mile//math.lcm(fuel, eat))