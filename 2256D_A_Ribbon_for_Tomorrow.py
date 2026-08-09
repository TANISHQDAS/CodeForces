import sys
 
m = 998244353
mx = 1000005
fc = [1] * mx
ic = [1] * mx
for i in range(1, mx):
    fc[i] = (fc[i-1] * i) % m
ic[mx-1] = pow(fc[mx-1], m - 2, m)
for i in range(mx - 2, -1, -1):
    ic[i] = (ic[i+1] * (i + 1)) % m
 
def c(n, r):
    if r < 0 or r > n:
        return 0
    return fc[n] * ic[r] % m * ic[n-r] % m
 
def f():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    p = 1
    o = []
    for _ in range(t):
        n = int(d[p])
        s = d[p+1]
        p += 2
        b = []
        k = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                k += 1
            else:
                b.append(k)
                k = 1
        b.append(k)
        
        so = sum(b[i] for i in range(0, len(b), 2))
        ko = (len(b) + 1) // 2
        se = sum(b[i] for i in range(1, len(b), 2))
        ke = len(b) // 2
        
        w1 = c(so - 1, ko - 1)
        w2 = c(se - 1, ke - 1) if ke > 0 else 1
        ans = (w1 * w2) % m
        o.append(str(ans))
        
    print('\n'.join(o))
 
if __name__ == '__main__':
    f()