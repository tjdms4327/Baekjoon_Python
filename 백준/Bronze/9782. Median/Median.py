case = 0
while True:
    case += 1
    length, *num = list(map(int, input().split()))

    if length==0:
        break
    elif length % 2 == 0:
        med = (num[length // 2] + num[length // 2 - 1]) / 2   
    else:
        med = num[length // 2]
    
    print(f"Case {case}: {med:.1f}")
