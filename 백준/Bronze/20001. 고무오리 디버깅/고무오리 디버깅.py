# bronzeII_20001
import sys

question = 0
start = input()
for line in sys.stdin.read().splitlines():
    if line == '고무오리 디버깅 끝':
        if question == 0:
            print('고무오리야 사랑해')
        else:
            print('힝구')
        break
    
    if line == '문제':
        question += 1
    else: # '고무오리'
        if question == 0:
            question += 2
        else:
            question -= 1