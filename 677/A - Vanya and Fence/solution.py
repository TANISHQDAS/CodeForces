n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
  if m>=a[i]:
    c+=1
  else:
    c+=2
 
print(c)    