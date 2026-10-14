n=int(input())
s=""
for i in range(1,n+1):
    s+="I hate" if i%2 else "I love"
    s+=" that " if i<n else " it"
print(s)