t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    b=1
    for k in range(1,n):
        if s[k]!=s[k-1]:
            b+=1
    m=0
    for i in range(1,n-1):
        if s[i]!=s[i-1] and s[i]!=s[i+1]:
            d=2 if s[i-1]==s[i+1] else 1
            if d>m:
                m=d
    print(b-m)