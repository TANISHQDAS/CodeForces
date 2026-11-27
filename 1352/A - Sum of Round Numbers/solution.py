for _ in range(int(input())):
    n=input()
    s=len(n)
    a=[]
    for i in range(s):
        x=int(n[i])*10**(s-i-1)
        if x:
            a.append(x)
    print(len(a))
    print(*a)