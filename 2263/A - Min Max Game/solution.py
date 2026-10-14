t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    o = sum(a)
    z = n - o
    
    if o >= z:
        print("Bessie")
    else:
        print("Elsie")