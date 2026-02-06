import sys
input = sys.stdin.readline

x, y, p, a, b = map(int, input().split())

sell = [x//y] * y
for i in range(1, x%y+1):
    sell[-i] += 1 


cost = 0 # 마지막 날 전까지 0병씩 팔기

p = p + b*(y-1) # 마지막 날 첫 병의 가격
cost += x*p - (x*(x-1)*a)//2

print(cost)