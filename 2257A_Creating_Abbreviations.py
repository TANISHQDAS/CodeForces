import sys
 
def s():
    d = sys.stdin.read().split()
    if not d:
        return
    it = iter(d)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        st = set()
        for _ in range(n):
            w = next(it)
            st.add(w[0].upper())
        ab = []
        for _ in range(m):
            ab.append(next(it))
        while True:
            nx = []
            ok = False
            for x in ab:
                if all(c in st for c in x):
                    st.add(x[0])
                    ok = True
                else:
                    nx.append(x)
            ab = nx
            if not ok:
                break
        if not ab:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))
 
s()