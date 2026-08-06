import sys
 
def mn():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    M = 10**9 + 7
    N = 105
    f = [0] * N
    f[0] = 1
    f[1] = 1
    for i in range(2, N):
        f[i] = (f[i-1] + 2 * f[i-2]) % M
    S = [0] * N
    S[0] = f[0]
    for i in range(1, N):
        S[i] = (S[i-1] + f[i]) % M
    o = []
    for k in range(1, t + 1):
        n = int(d[k])
        B = n.bit_length()
        bs = S[B-3] if B >= 3 else 0
        b2 = (n >> (B-2)) & 1 if B >= 2 else 0
        if B >= 2 and b2 == 0:
            o.append(bs % M)
            continue
        cF, cT = 1, 0
        tt = 0
        j = B - 3
        while j >= 0:
            nb = (n >> j) & 1
            nF, nT = 0, 0
            if nb == 1:
                nF += cT
            if j >= 1:
                fj = f[j]
                fm = f[j-1]
            else:
                fj = f[0]
                fm = 0
            if nb == 0:
                nF += cF
                if j >= 1:
                    nT += cF
            else:
                tt = (tt + cF * fj) % M
                if j >= 1:
                    tt = (tt + cF * fm) % M
                    nT += cF
            cF, cT = nF % M, nT % M
            j -= 1
        tt = (tt + cF) % M
        o.append((bs + tt) % M)
    sys.stdout.write('\n'.join(map(str, o)) + '\n')
 
if __name__ == '__main__':
    mn()