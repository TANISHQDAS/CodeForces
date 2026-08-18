import sys
from bisect import bisect_right as br
 
def f():
    dt = sys.stdin.read().split()
    if not dt:
        return
    it = iter(dt)
    t = int(next(it))
    o = []
    
    for _ in range(t):
        s = int(next(it))
        q = int(next(it))
        
        sq = int(s**0.5)
        d = []
        for i in range(1, sq + 1):
            if s % i == 0:
                d.append(i)
                if i * i != s:
                    d.append(s // i)
        d.sort()
        
        sz = len(d)
        w = [0] * (sz + 2)
        h = [0] * (sz + 2)
        pr = [0] * (sz + 2)
        
        for i in range(sz):
            w[i+1] = d[i]
            
        w[sz+1] = 200000000000000
        
        for i in range(1, sz + 1):
            h[i] = s // w[i]
            pr[i] = pr[i-1] + (w[i] - w[i-1]) * h[i]
            
        for _ in range(q):
            x = int(next(it))
            y = int(next(it))
            
            p = br(w, x) - 1
            m = br(w, s // y) - 1
            
            if p < m:
                o.append(str(x * y))
            else:
                a = w[m] * y + pr[p] - pr[m] + (x - w[p]) * h[p+1]
                o.append(str(a))
                
    sys.stdout.write("\n".join(o) + "\n")
 
if __name__ == '__main__':
    f()