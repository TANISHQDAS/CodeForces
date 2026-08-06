import sys
 
 
def sol():
    inp = sys.stdin.read().split()
    if not inp:
        return
    idx = 0
    tst = int(inp[idx])
    idx += 1
    out = []
 
    for _ in range(tst):
        r = int(inp[idx])
        c = int(inp[idx + 1])
        idx += 2
 
        v = [int(inp[idx + i]) for i in range(r)]
        idx += r
 
        g = []
        for i in range(r):
            g.append([int(inp[idx + j]) for j in range(c)])
            idx += c
 
        if c == 1:
            out.append("1")
            continue
 
        u = sorted(list(set(x for row in g for x in row)), reverse=True)
        m = len(u)
        p = {x: i + 1 for i, x in enumerate(u)}
 
        s = [0] * (m + 1)
        k = [0] * (m + 1)
 
        tot = 0
        ans = c
        b = 1 << (m.bit_length() - 1) if m > 0 else 0
 
        for i in range(r - 1, -1, -1):
            for x in g[i]:
                tot += x
                idx2 = p[x]
                while idx2 <= m:
                    s[idx2] += x
                    k[idx2] += 1
                    idx2 += idx2 & -idx2
 
            req = v[i]
            if req <= tot:
                j = 0
                cur = 0
                cnt = 0
                step = b
                while step > 0:
                    if j + step <= m and cur + s[j + step] < req:
                        cur += s[j + step]
                        cnt += k[j + step]
                        j += step
                    step >>= 1
 
                rem = req - cur
                val = u[j]
                ext = (rem + val - 1) // val
                req_cnt = cnt + ext
                if req_cnt < ans:
                    ans = req_cnt
                    if ans == 1:
                        break
 
        out.append(str(ans))
 
    sys.stdout.write("\n".join(out) + "\n")
 
 
if __name__ == "__main__":
    sol()