# bronzeIV_34400
t = int(input())
for _ in range(t):
    time = int(input())
    now = (time + 0.5) % 25
    if now <= 17:
        print('ONLINE')
    else:
        print('OFFLINE')