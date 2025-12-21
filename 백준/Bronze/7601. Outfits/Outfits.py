import sys
input = sys.stdin.readline

scenario = 0
while True:   
    n, d = map(int, input().split())
    if n==d==0:
        break
    scenario += 1
    print(f'Scenario {scenario}')
    
    del_b = int(input())
    becs_del_pos = del_b if del_b != 0 else None
    del_c = int(input())   
    cas_del_pos = (n - del_c + 1) if del_c != 0 else None
    
    for day in range(1, d + 1):
        b, c = map(int, input().split())

        real_b = b
        if becs_del_pos is not None and b >= becs_del_pos:
            real_b += 1
        real_c = n - c + 1
        if cas_del_pos is not None and real_c <= cas_del_pos:
            real_c -= 1

        if real_b == real_c:
            print(f"Day {day} ALERT")
        else:
            print(f"Day {day} OK")
        