import sys
 
 
def sol():
    inp = sys.stdin.read().split()
    if not inp:
        return
    t = int(inp[0])
    p = 1
    out = []
 
    for _ in range(t):
        n = int(inp[p])
        p += 1
        b = [int(x) for x in inp[p : p + n]]
        p += n
 
        fr = {}
        for x in b:
            fr[x] = fr.get(x, 0) + 1
 
        u = sorted(fr.keys())
        k = len(u)
 
        if u[0] != 0:
            out.append("-1")
            continue
 
        ok = True
        v = [0] * k
 
        for i in range(k - 1):
            df = u[i + 1] - u[i]
            c = fr[u[i]]
            if df % c != 0:
                ok = False
                break
            v[i] = df // c
 
        if not ok:
            out.append("-1")
            continue
 
        if k > 1 and v[0] < 1:
            out.append("-1")
            continue
 
        for i in range(k - 2):
            if v[i] >= v[i + 1]:
                ok = False
                break
 
        if not ok:
            out.append("-1")
            continue
 
        if k == 1:
            v[0] = 1
        else:
            v[k - 1] = v[k - 2] + 1
 
        mp = {u[i]: v[i] for i in range(k)}
        res = [str(mp[x]) for x in b]
        out.append(" ".join(res))
 
    print("\n".join(out))
 
 
if __name__ == "__main__":
    sol()