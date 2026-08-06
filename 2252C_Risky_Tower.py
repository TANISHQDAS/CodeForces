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
 
        v = [int(x) for x in inp[idx : idx + r]]
        idx += r
 
        if c == 1:
            out.append("1")
            idx += r
            continue
 
        raw = [int(x) for x in inp[idx : idx + r * c]]
        idx += r * c
 
        u = sorted(list(set(raw)), reverse=True)
        m = len(u)
        p = {x: i + 1 for i, x in enumerate(u)}
 
        s = [0] * (m + 1)
        k = [0] * (m + 1)
 
        tot = 0
        ans = c
        b = 1 << (m.bit_length() - 1) if m > 0 else 0
 
        for i in range(r - 1, -1, -1):
            row_vals = raw[i * c : (i + 1) * c]
            for x in row_vals:
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
                req_cnt = cnt + (rem + val - 1) // val
                if req_cnt < ans:
                    ans = req_cnt
                    if ans == 1:
                        break
 
        out.append(str(ans))
 
    sys.stdout.write("\n".join(out) + "\n")
 
 
if __name__ == "__main__":
    sol()