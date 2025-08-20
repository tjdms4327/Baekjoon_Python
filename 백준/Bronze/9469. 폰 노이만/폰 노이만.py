t = int(input())
for _ in range(t):
    n, d, a, b, f = map(float, input().split())
    fly = (d / (a + b)) * f # '거 = 속 * 시' 공식 이용
    print(f'{int(n)} {fly:.6f}')