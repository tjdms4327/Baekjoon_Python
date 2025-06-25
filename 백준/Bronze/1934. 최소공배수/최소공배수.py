import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    gcd = math.gcd(a, b)  
    lcm = (a * b) // gcd 
    
    print(lcm)
