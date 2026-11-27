n=int(input())
c=0
for i in [100,20,10,5,1]:
    c+=n//i
    n%=i
print(c)