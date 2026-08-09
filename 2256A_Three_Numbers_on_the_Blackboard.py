import sys
 
def f():
    d = sys.stdin.read().split()
    if not d:
        return
    t = int(d[0])
    p = 1
    o = []
    for _ in range(t):
        x = int(d[p])
        y = int(d[p+1])
        z = int(d[p+2])
        p += 3
        l = sorted([x, y, z])
        o.append(str(min(l[2] - l[0], l[1])))
    print('\n'.join(o))
 
if __name__ == '__main__':
    f()