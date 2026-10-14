s=input().lower()
 
v="aoyeui"
ans=""
 
for x in s:
    if x not in v:
        ans+="."+x
 
print(ans)