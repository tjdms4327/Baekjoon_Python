# bronzeII_2520
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input() 
    milk, egg, sugar, salt, flour = map(int, input().split())
    banana, jam, chocolate, walnut = map(int, input().split())
    
    x = min(milk/8, egg/8, sugar/4, salt/1, flour/9)
    plain = int(16 * x)
    topping = banana + jam//30 + chocolate//25 + walnut//10
    print(min(plain, topping))
