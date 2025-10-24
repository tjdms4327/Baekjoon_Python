# bronzeI_3023
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
card_leftup = [list(input().strip()) for _ in range(r)]

full_card = []
for row in card_leftup:
    full_card.append(list(row + row[::-1]))
for row in full_card[::-1]:
    full_card.append(list(row))

error_r, error_c = map(int, input().split())
error_r -= 1; error_c -= 1

if full_card[error_r][error_c] == '#':
    full_card[error_r][error_c] = '.'
else:
    full_card[error_r][error_c] = '#'

for row in full_card:
    print(''.join(row))