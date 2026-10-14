import sys
 
def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); c = int(data[idx+1]); idx += 2
        a = list(map(int, data[idx:idx+n])); idx += n
        a.sort()
        total = sum(a)
        baseline = total - c * n
        cnt = 0
        while cnt < n and a[cnt] < c:
            cnt += 1
        p = min(cnt, n // 2)
        gain = c * p - sum(a[:p])
        out.append(str(baseline + gain))
    print('
'.join(out))
 
solve()