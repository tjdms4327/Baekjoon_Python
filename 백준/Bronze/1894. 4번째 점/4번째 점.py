import sys
input = sys.stdin.readline

while True:
    s = input().split()
    if not s:
        break

    a = list(map(float, s))
    pts = [
        (a[0], a[1]),
        (a[2], a[3]),
        (a[4], a[5]),
        (a[6], a[7])
    ]

    # 공통점 찾기
    for p in pts:
        if pts.count(p) == 2:
            common = p
            break

    x = 0
    y = 0
    for p in pts:
        if p != common:
            x += p[0]
            y += p[1]

    x -= common[0]
    y -= common[1]

    print(f"{x:.3f} {y:.3f}")
