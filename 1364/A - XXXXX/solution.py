t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    total=sum(a)
    if total%x!=0:
        print(n)
        continue
    left=-1
    right=-1
    for i in range(n):
        if a[i]%x!=0:
            left=i
            break
    for i in range(n-1,-1,-1):
        if a[i]%x!=0:
            right=i
            break
    if left==-1:
        print(-1)
    else:
        print(n-min(left+1,n-right))