import sys
input = sys.stdin.readline

for a in range(1, 10):
    print("? A", a, flush=True)
    resp = int(input())

    if resp == 1:
        for b in range(1, 10):
            print("? B", b, flush=True)
            resp_b = int(input())
            if resp_b == 1:
                print("!", a + b)
                break
        break