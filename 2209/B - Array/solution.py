import sys
import bisect
input=sys.stdin.readline
 
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=[]
    res=[0]*n
    for i in range(n-1,-1,-1):
        x=a[i]
        pos=bisect.bisect_left(s,x)
        less=pos
        greater=len(s)-bisect.bisect_right(s,x)
        res[i]=max(less,greater)
        bisect.insort(s,x)
    print(*res)