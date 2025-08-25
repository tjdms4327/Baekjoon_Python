import sys
input = sys.stdin.readline

city, min_t = '', 201
while True:
    c, t = input().strip().split()
    t = int(t)
    if t < min_t:
        city = c
        min_t = t

    if c =='Waterloo': break
print(city)