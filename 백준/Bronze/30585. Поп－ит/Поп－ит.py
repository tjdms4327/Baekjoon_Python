h, w = map(int, input().split())

one_bubbles, zero_bubbles = 0, 0
for _ in range(h):
    bubble=input()
    one_bubbles+=bubble.count('1')
    zero_bubbles+=bubble.count('0')
print(min(one_bubbles, zero_bubbles))