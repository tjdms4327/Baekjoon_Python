import sys
input = sys.stdin.readline

for _ in range(int(input())):
    red, green, blue = 0, 0, 0
    for _ in range(10):
        r, g, b = map(int, input().split())
        red += r ; green += g ; blue += b

    r_avg = int(red / 10 + 0.5)
    g_avg = int(green / 10 + 0.5)
    b_avg = int(blue / 10 + 0.5)
    print(r_avg, g_avg, b_avg)