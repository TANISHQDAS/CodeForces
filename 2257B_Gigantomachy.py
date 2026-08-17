import sys
 
def f():
    d = sys.stdin.read().split()
    if not d:
        return
    it = iter(d)
    t = int(next(it))
    o = []
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        b = [int(next(it)) for _ in range(m)]
        p = 0
        h = a[0]
        q = 0
        w = b[0]
        while True:
            u = h - a[p + 1] + 1 if p < n - 1 else h
            v = w - b[q + 1] + 1 if q < m - 1 else w
            k = min(u, v)
            h -= k
            w -= k
            if v <= u:
                if q < m - 1:
                    q += 1
                    w = b[q]
                else:
                    o.append("1")
                    break
            if u <= v:
                if p < n - 1:
                    p += 1
                    h = a[p]
                else:
                    o.append("2")
                    break
    print("\n".join(o))
 
f()