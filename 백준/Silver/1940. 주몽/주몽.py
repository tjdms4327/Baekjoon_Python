import sys
input = sys.stdin.readline

n = int(input()) # 재료 개수
m = int(input()) # 갑옷 완성되는 번호 합
ingredients = list(map(int, input().split()))
ingredients.sort()

count = 0
start, end = 0, n - 1
while start < end:
    sum = ingredients[start] + ingredients[end]
    if sum < m:
        start += 1
    elif sum > m:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1
print(count)