import sys
input = sys.stdin.readline

r, g, b = map(int, input().split())
c_r, c_g, c_b = map(int, input().split())
c_rg, c_gb = map(int, input().split())

need_r = max(0, r - c_r)
need_g = max(0, g - c_g)
need_b = max(0, b - c_b)

used = 0

# 빨강
use = min(need_r, c_rg)
need_r -= use
c_rg -= use
used += use

if need_r > 0:
    print(-1)
    sys.exit()

# 초록
use = min(need_g, c_rg)
need_g -= use
c_rg -= use
used += use

use = min(need_g, c_gb)
need_g -= use
c_gb -= use
used += use

if need_g > 0:
    print(-1)
    sys.exit()

# 파랑
use = min(need_b, c_gb)
need_b -= use
c_gb -= use
used += use

if need_b > 0:
    print(-1)
    sys.exit()

print(used)