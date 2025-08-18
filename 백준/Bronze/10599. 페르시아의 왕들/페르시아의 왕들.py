while True:
    years = list(map(int, input().split()))
    if years == [0, 0, 0, 0]:
        break
    years.sort()

    print(years[-2] - years[1], years[-1] - years[0])