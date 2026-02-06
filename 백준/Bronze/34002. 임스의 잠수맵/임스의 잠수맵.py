import sys, math
input = sys.stdin.readline

c, a, b = map(int, input().split())
s, v = map(int, input().split())
l = int(input())

left_level = 250 - l
exp = left_level * 100

if a <= c and b <= c: # c가 최대
    time = math.ceil(exp / c)
else:
    if a < b: # a가 최대가 되도록 조정
        a, b = b, a
        s, v = v, s 
        
    if exp <= 30*s*a: # a로 다 처리될 때
        time = math.ceil(exp/a)
        exp = 0
    else:
        time = 30*s
        exp -= 30*s*a
        
    if exp > 0:
        if b <= c:
            time += math.ceil(exp/c)
        else: # b > c
            if exp <= 30*v*b: # b로 다 처리될 때
                time += math.ceil(exp/b)
                exp = 0
            else:
                time += 30*v
                exp -= 30*v*b
                
            if exp > 0:
                time += math.ceil(exp/c)

print(time)