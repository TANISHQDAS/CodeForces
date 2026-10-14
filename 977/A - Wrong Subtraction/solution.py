n,m=list(map(int,input().split()))
for _ in range(m):
  if n%10==0:
    n=n//10
  else:
    n=n-1
 
print(n)    