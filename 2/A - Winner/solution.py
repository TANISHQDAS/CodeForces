import sys
 
def f():
    a = sys.stdin.read().splitlines()
    if not a:
        return
    n = int(a[0])
    r = []
    t = {}
    for i in range(1, n + 1):
        u, v = a[i].split()
        v = int(v)
        r.append((u, v))
        t[u] = t.get(u, 0) + v
    
    m = max(t.values())
    w = {k for k, x in t.items() if x == m}
    
    c = {}
    for u, v in r:
        c[u] = c.get(u, 0) + v
        if c[u] >= m and u in w:
            print(u)
            break
 
f()