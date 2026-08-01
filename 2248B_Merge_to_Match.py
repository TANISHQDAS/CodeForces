import sys
inp = sys.stdin.read().split()
idx = 0
t = int(inp[idx]); idx += 1
out = []
for _ in range(t):
    n, m = int(inp[idx]), int(inp[idx+1]); idx += 2
    a = inp[idx:idx+n]; idx += n
    b = inp[idx:idx+m]; idx += m
    a = sorted(map(int, a))
    b = sorted(map(int, b))
    ok = n >= 2 * m
    if ok:
        for i in range(m):
            if not (a[i] < b[i]):
                ok = False
                break
    if ok:
        for i in range(m):
            if not (a[n - m + i] > b[i]):
                ok = False
                break
    out.append("YES" if ok else "NO")
print('\n'.join(out))