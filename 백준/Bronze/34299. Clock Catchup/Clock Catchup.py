import sys
input = sys.stdin.readline

def to_seconds(t):
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s

t1 = to_seconds(input().strip())
t2 = to_seconds(input().strip())

# 60초마다 12 도달
second_hits = t2 // 60 - t1 // 60
# 3600초마다 12 도달
minute_hits = t2 // 3600 - t1 // 3600
# 12시간(43200초)마다 12 도달
hour_hits = t2 // 43200 - t1 // 43200

print(hour_hits, minute_hits, second_hits)