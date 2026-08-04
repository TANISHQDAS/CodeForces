for _ in range(int(input())):
    a=list(map(int,input().split()))
    r=0
    while len(set(a))==3:
        i=a.index(max(a))
        j=a.index(min(a))
        a[i]-=1
        a[j]+=1
        r+=1
    print(r)