t=int(input())
for _ in range(t):
    n=int(input())
    if n<31:
        print("NO")
    else:
        if n==36 or n==40 or n==44:
            print("YES")
            print(6,10,15,n-31)
        else:
            print("YES")
            print(6,10,14,n-30)