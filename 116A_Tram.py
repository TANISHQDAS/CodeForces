n=int(input())
c=0
t=0
for _ in range(n):
  a,b=map(int,input().split())
  c-=a
  c+=b
  t=max(t,c)
 
print(t)