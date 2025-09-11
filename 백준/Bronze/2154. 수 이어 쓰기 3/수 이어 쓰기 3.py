import sys
input = sys.stdin.readline

find = input().strip()
len_find = len(find)

s_window = ''
i = 1
pos = 0 # 현재 숫자까지 몇 글자 쌓였는지
while True:
    for c in str(i):
        s_window += c
        pos += 1

        # 윈도우 길이 유지
        if len(s_window) > len_find:
            s_window = s_window[1:]
        if s_window == find:
            print(pos - len_find + 1)
            sys.exit()
    i += 1