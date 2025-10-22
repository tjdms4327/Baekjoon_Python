# bronzeI_15947
import sys
input = sys.stdin.readline

song = ['baby', 'sukhwan', 'tururu', 'turu',
        'very', 'cute', 'tururu', 'turu',
        'in', 'bed', 'tururu', 'turu',
        'baby', 'sukhwan']

n = int(input())

reminder = (n-1) % len(song)
cand = song[reminder]
if cand in ['turu', 'tururu']:
    k = n//len(song) + cand.count('ru')
    if k >= 5:
        print(f'tu+ru*{k}')
        sys.exit()
    else:
        cand = 'tu' + 'ru' * k
print(cand)