def f(q):
 m=len(q)
 if m==1:
  return 2 if q[0]=='?' else 1
 d=[[0,0] for _ in range(m)]
 if q[0]=='?':
  d[0]=[1,1]
 elif q[0]=='0':
  d[0]=[1,0]
 else:
  d[0]=[0,1]
 for i in range(1,m):
  if q[i]=='?':
   d[i][0]=d[i-1][1]
   d[i][1]=d[i-1][0]
  elif q[i]=='0':
   d[i][0]=d[i-1][1]
  else:
   d[i][1]=d[i-1][0]
 return d[m-1][0]+d[m-1][1]
t=int(input())
for _ in range(t):
 n=int(input())
 s=input()
 e=[s[i] for i in range(0,n,2)]
 o=[s[i] for i in range(1,n,2)]
 print(f(e)*f(o)%998244353)