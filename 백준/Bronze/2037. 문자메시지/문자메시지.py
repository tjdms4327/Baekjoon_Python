# bronzeI_2037
import sys
input = sys.stdin.readline

p, w = map(int, input().split())
s = input().strip()

button_press = {}
key_map = {
    '1': ' ',
    '2': 'ABC', '3': 'DEF',
    '4': 'GHI', '5': 'JKL', '6': 'MNO',
    '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
}

for btn, chars in key_map.items():
    for i, ch in enumerate(chars):
        button_press[ch] = (btn, i + 1)

time = 0
prev_btn = None

for ch in s:
    btn, presses = button_press[ch.upper()] 
    if prev_btn == btn and ch != ' ':
        time += w
    time += p * presses
    prev_btn = btn

print(time)

