import sys
input = sys.stdin.readline

while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break

    diag = h**2 + w**2
    best = (float('inf'), float('inf'), float('inf'))  # (대각선, H, W)
    for H in range(1, 151):
        for W in range(H + 1, 151):  # 넓은 직사각형 조건 W > H
            d = H**2 + W**2

            if d > diag or (d == diag and H > h):
                # 최소 대각선, 같으면 H 최소
                if d < best[0] or (d == best[0] and H < best[1]):
                    best = (d, H, W)

    print(best[1], best[2])