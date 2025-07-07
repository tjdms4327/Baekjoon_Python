socks=[]
for _ in range(5):
    sock=int(input())
    if sock in socks:
        socks.remove(sock)
    else:
        socks.append(sock)
print(*socks)