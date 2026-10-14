s=input()
 
x="hello"
j=0
 
for c in s:
    if j<5 and c==x[j]:
        j+=1
 
if j==5:
    print("YES")
else:
    print("NO")