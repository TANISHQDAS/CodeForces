import sys
from bisect import bisect_left as bl
 
 
def sol():
    inp = sys.stdin.read().split()
    if not inp:
        return
    t = int(inp[0])
    ptr = 1
    out = []
    for _ in range(t):
        n = int(inp[ptr])
        ptr += 1
        b = [int(x) for x in inp[ptr : ptr + n]]
        ptr += n
        if sum(b) <= 0:
            out.append("-1")
            continue
        b.sort()
        p = list(range(n + 1))
 
        def fn(i):
            pth = []
            while p[i] != i:
                pth.append(i)
                i = p[i]
            for x in pth:
                p[x] = i
            return i
 
        sm = 0
        a = []
        for _ in range(n):
            pos = bl(b, 1 - sm)
            pos = fn(pos)
            x = b[pos]
            sm += x
            a.append(str(sm))
            p[pos] = fn(pos + 1)
        out.append(" ".join(a))
    print("\n".join(out))
 
 
if __name__ == "__main__":
    sol()