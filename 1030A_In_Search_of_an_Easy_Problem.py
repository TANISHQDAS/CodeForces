n=int(input())
a=list(map(int,input().split()))
c=0
 
for i in range(n):
  if a[i]==1:
    c+=1
    break
 
if c==1:
  print("Hard")
else:
  print("Easy")
  