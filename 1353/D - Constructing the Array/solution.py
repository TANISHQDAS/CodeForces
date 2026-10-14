import heapq
 
t=int(input())
for _ in range(t):
    n=int(input())
    a=[0]*n
    heap=[(-n,0,n-1)]
    for i in range(1,n+1):
        l,r=heapq.heappop(heap)[1:]
        if (r-l+1)%2:
            mid=(l+r)//2
        else:
            mid=(l+r-1)//2
        a[mid]=i
        if l<=mid-1:
            heapq.heappush(heap,(-(mid-l),l,mid-1))
        if mid+1<=r:
            heapq.heappush(heap,(-(r-mid),mid+1,r))
    print(*a)