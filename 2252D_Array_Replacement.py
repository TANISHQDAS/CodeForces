import sys
input = sys.stdin.readline
 
def slv(a, n):
    b = [a[i] - a[i - 1] for i in range(1, n)]
    m = len(b)
    i = 0
    while i < m:
        j = i
        par = b[i] & 1
        while j < m and (b[j] & 1) == par:
            j += 1
        b[i:j] = sorted(b[i:j])
        i = j
    res = [a[0]]
    cur = a[0]
    for x in b:
        cur += x
        res.append(cur)
    return res
 
def main():
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        out.append(' '.join(map(str, slv(a, n))))
    sys.stdout.write('\n'.join(out) + '\n')
 
main()