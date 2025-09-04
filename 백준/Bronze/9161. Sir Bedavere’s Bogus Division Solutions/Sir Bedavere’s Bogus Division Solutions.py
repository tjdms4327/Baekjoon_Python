for numerator in range(100, 1000):
    for denominator in range(100, 1000):
        if numerator == denominator:  # trivial case 제외
            continue
        
        if numerator % 10 == denominator // 100:
            top = numerator // 10 
            bottom = denominator % 100
            if bottom == 0:
                continue
            if numerator / denominator == top / bottom:
                print(f'{numerator} / {denominator} = {top} / {bottom}')