n=int(input())
m=input()
 
a=m.count("A")
d=m.count("D")
 
if a>d:
  print("Anton")
elif d>a:
  print("Danik")
else:
  print("Friendship")