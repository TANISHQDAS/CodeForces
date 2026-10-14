import sys
 
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)
 
    if a == b:
        print(0)
        continue
 
    s = 2
    while True:
        ok = True
        for i in range(0, n, s):
            if sorted(a[i:i + s]) != sorted(b[i:i + s]):
                ok = False
                break
        if ok:
            print(s // 2)
            break
        s *= 2