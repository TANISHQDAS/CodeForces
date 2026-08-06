import sys as v
 
 
def f():
    u = v.stdin.read().split()
    if not u:
        return
    t = int(u[0])
    p = 1
    o = []
    for g in range(t):
        n = int(u[p])
        w = u[p + 1]
        p += 2
        a = b = c = d = 0
        x = y = 0
        for i in w:
            if i == "0":
                x += 1
                a = b + 1 if b else 1
                c = d + 1 if d else c
            else:
                y += 1
                b = a + 1 if a else b
                d = c + 1 if c else 1
        z = x - y
        if z > 2 or z < -2:
            o.append("-1")
        elif z == 2:
            o.append(str(n - a))
        elif z == 1:
            o.append(str(n - max(a, b, c, 0)))
        elif z == 0:
            o.append(str(n - max(a, b, c, d, 0)))
        elif z == -1:
            o.append(str(n - max(d, b, c, 0)))
        else:
            o.append(str(n - d))
    v.stdout.write("\n".join(o) + "\n")
 
 
if __name__ == "__main__":
    f()