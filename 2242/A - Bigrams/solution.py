t = int(input())
 
for _ in range(t):
    k = int(input())
    c = list(map(int, input().split()))
 
    kinds = 0
    two = 0
    ok = False
 
    for x in c:
        if x > 0:
            kinds += 1
        if x >= 2:
            two += 1
 
    if kinds == 1:
        if max(c) >= 3:
            print("YES")
        else:
            print("NO")
        continue
 
    for x in c:
        if x >= 4:
            ok = True
            break
 
    if not ok:
        for x in c:
            if x == 3:
                ok = True
                break
 
    if not ok and two >= 2:
        ok = True
 
    if ok:
        print("YES")
    else:
        print("NO")