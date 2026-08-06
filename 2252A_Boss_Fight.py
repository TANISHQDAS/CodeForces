from collections import Counter
 
def slv(a, n):
    c = Counter(a)
    m = max(c.values())
    tot = sum(a)
    if m <= (n + 1) // 2:
        return tot
    v = next(x for x in c if c[x] == m)
    w = 2 * m - n - 2
    return tot - w * v
 
t = int(input())
res = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res.append(str(slv(a, n)))
print('\n'.join(res))