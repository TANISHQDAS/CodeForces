t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ok=False
    for i in range(1,1<<n):
        p=1
        for j in range(n):
            if i>>j&1:
                p*=a[j]
        if p==67:
            ok=True
            break
    print("YES" if ok else "NO")