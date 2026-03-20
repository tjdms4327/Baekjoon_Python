import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    unknown = s.count('?')

    count_U = s.count('U')
    count_D = s.count('D')
    count_R = s.count('R')
    count_L = s.count('L')

    min_x = - (count_L + unknown)
    max_x = count_R + unknown
    min_y = - (count_D + unknown)
    max_y = count_U + unknown

    min_x = -count_L - unknown + count_R
    max_x = count_R + unknown - count_L
    min_y = -count_D - unknown + count_U
    max_y = count_U + unknown - count_D

    print(min_x, min_y, max_x, max_y)