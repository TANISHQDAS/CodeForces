n=int(input())
a=input()
c=1
 
for i in range(n-1):
    b=input()
    if a!=b:
        c+=1
    a=b
 
print(c)
    
  