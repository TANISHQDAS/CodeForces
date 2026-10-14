for _ in range(int(input())):
    a,b= map(int,input().split())
    if a<=b:
        print("-1")
    else:
        print(min(a-b,b))    