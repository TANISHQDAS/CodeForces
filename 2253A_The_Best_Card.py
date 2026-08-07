def p(n):
 if n<2:return 0
 if n==2:return 1
 if n%2==0:return 0
 i=3
 while i*i<=n:
  if n%i==0:return 0
  i+=2
 return 1
t=int(input())
for _ in range(t):
 n=int(input())
 print("YES"if p(n+1)else"NO")