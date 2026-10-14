import sys
input=sys.stdin.readline
 
t=int(input())
for _ in range(t):
    n,c,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(n):
        if a[i]>c:
            break
        cap=c-a[i]
        x=min(cap,k)
        k-=x
        c+=a[i]+x
    print(c)