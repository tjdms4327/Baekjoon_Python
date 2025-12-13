import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())
for _ in range(k):
    s, t, r = map(int, input().split())
    tot_page = n
    t_page = s * t
    
    time = 0
    while tot_page > t_page:
        time += t + r
        tot_page -= t_page
    time += tot_page/s
    print(math.ceil(time))