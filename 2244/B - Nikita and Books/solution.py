import sys
 
def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx+n]; idx += n
        a = list(map(int, a))
        prefix = 0
        ok = True
        for k in range(1, n+1):
            prefix += a[k-1]
            need = k*(k+1)//2
            if prefix < need:
                ok = False
        out.append("YES" if ok else "NO")
    print('
'.join(out))
 
solve()