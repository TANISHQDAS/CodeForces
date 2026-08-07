import sys
import math
 
def f():
    d = sys.stdin.read().split()
    if not d:
        return
    TestsNumT = int(d[0])
    idx = 1
    o = []
    for _ in range(TestsNumT):
        x = int(d[idx])
        y = int(d[idx+1])
        idx += 2
        
        n = (math.isqrt(8 * (x + y) + 1) - 1) // 2
        s = n * (n + 1) // 2
        
        l = max(0, s - y)
        r = min(s, x)
        
        idf = (s + x - y) // 2
        
        md = -1
        bp = -1
        
        for p in (idf, idf + 1):
            pc = min(max(p, l), r)
            qc = s - pc
            dst = (x - pc) ** 2 + (y - qc) ** 2
            
            if md == -1 or dst < md:
                md = dst
                bp = pc
                
        pn = bp
        
        ba = -1
        start_a = max(0, int(math.isqrt(2 * pn)) - 2)
        for a in range(start_a, n + 1):
            mip = a * (a + 1) // 2
            map_val = n * a - a * (a - 1) // 2
            if mip <= pn <= map_val:
                ba = a
                break
                
        a = ba
        c = [i for i in range(1, a + 1)]
        rm = pn - a * (a + 1) // 2
        
        for i in range(a - 1, -1, -1):
            ad = min(rm, n - a)
            c[i] += ad
            rm -= ad
            
        ans = ['Y'] * n
        for i in range(a):
            pos = n - c[i] + 1
            ans[pos - 1] = 'X'
            
        o.append("".join(ans))
        
    print("\n".join(o))
 
if __name__ == '__main__':
    f()