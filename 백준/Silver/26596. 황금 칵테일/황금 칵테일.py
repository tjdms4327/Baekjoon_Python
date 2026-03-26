import sys, math
input = sys.stdin.readline

m = int(input())

ingredients = {}
for _ in range(m):
    s, x = input().strip().split()
    x = int(x)
    
    if s in ingredients:
        ingredients[s] += x
    else:
        ingredients[s] = x

ml = list(ingredients.values())
ml.sort()

for i in range(len(ml)):
    if math.floor(ml[i]*1.618) in ml[:i]+ml[i+1:]:
        print('Delicious!')
        sys.exit()

print('Not Delicious...')