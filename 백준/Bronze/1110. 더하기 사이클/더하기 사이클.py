def cycle(num, origin, length):
    if num<10:
        result=11*num
    else:
        n10=num//10
        n1=num%10
        r1=n10+n1
        result=r1%10 + n1*10
    length+=1
    #print(length, result, origin)
    if result==origin:
        print(length)
        return length
    cycle(result, origin, length)

if __name__=="__main__":
    num=int(input())
    cycle(num,num,0)