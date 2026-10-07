n=int(input())
 
for i in range(1,n+1):
    s=str(i)
    if all(x in "47" for x in s):
        if n%i==0:
            print("YES")
            break
else:
    print("NO")
   
 