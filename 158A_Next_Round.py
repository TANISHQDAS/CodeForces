n, k = map(int, input().split())
a = list(map(int, input().split()))
 
c = a[k - 1]
ans = 0
 
for x in a:
    if x >= c and x > 0:
        ans += 1
 
print(ans)