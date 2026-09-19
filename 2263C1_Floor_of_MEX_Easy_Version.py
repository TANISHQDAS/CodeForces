import sys
d=sys.stdin.buffer.read().split()
p=0
t=int(d[p]);p+=1
out=[]
for _ in range(t):
    n=int(d[p]);p+=1
    a=list(map(int,d[p:p+n]));p+=n
    df=[0]*(n+2)
    for i in range(n):
        k=i+1
        v=a[i]*k
        if v<n:
            r=v+k-1
            if r>=n:r=n-1
            df[v]+=1
            df[r+1]-=1
    frb=[False]*n
    c=0
    for i in range(n):
        c+=df[i]
        if c>0:frb[i]=True
    par=list(range(n+1))
    for i in range(n):
        if frb[i]:
            x=i+1
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            par[i]=x
    res=[]
    for i in range(n):
        k=i+1
        ak=a[i]
        for j in range(ak):
            l=j*k
            if l>=n:break
            r=l+k-1
            if r>=n:r=n-1
            x=l
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            if x<=r:
                res.append(x)
                y=x+1
                while par[y]!=y:
                    par[y]=par[par[y]]
                    y=par[y]
                par[x]=y
    res.sort()
    out.append(str(len(res)))
    out.append(' '.join(map(str,res)))
sys.stdout.write('\n'.join(out)+'\n')