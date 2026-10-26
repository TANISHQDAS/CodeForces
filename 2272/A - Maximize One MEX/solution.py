for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=set()
    m=0
    f=[]
    for x in a:
        s.add(x)
        while m in s:
            m+=1
        f.append(m)
    bst=sorted(f,reverse=True)[k-1]
    ans=-1
    for i in range(n):
        for j in range(i+1,n):
            a[i],a[j]=a[j],a[i]
            s=set()
            m=0
            f=[]
            for x in a:
                s.add(x)
                while m in s:
                    m+=1
                f.append(m)
            v=sorted(f,reverse=True)[k-1]
            if v>bst:
                bst=v
                ans=f"{i+1} {j+1}"
            a[i],a[j]=a[j],a[i]
    print(ans)