import sys
 
def s():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    k = 1
    o = []
    for _ in range(t):
        n = int(d[k])
        k += 1
        p = []
        for _ in range(n):
            p.append((int(d[k]), int(d[k+1]), int(d[k+2]), int(d[k+3])))
            k += 4
        ans = 0
        for m in range(n, 0, -1):
            j = 1
            for l, r, u, v in p:
                if not (l <= j <= r or u <= m - j + 1 <= v):
                    j += 1
                    if j > m:
                        break
            if j > m:
                ans = m
                break
        o.append(str(ans))
    print('\n'.join(o))
 
if __name__ == '__main__':
    s()