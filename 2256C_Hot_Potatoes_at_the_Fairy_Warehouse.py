import sys
 
def f():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    p = 1
    o = []
    for _ in range(t):
        n = int(d[p])
        s = d[p+2]
        p += 3
        rs = 0
        bs = 0
        l = 2 * n
        for i in range(l):
            if s[i] == '1':
                nx = (i + 1) % l
                fp = nx if s[nx] == '0' else i
                if fp % 2 == 1:
                    rs += 1
                else:
                    bs += 1
        o.append(f"{rs} {bs}")
    print('\n'.join(o))
 
if __name__ == '__main__':
    f()