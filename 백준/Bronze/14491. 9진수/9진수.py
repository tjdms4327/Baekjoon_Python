import sys
input = sys.stdin.readline

t = int(input())

ans = ''
while t >= 9:
    temp = t % 9
    ans += str(temp)
    
    t //= 9
ans += str(t)

print(ans[::-1])