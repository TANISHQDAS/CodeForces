import sys
 
 
def sol():
    inp = sys.stdin.read().split()
    if not inp:
        return
    t = int(inp[0])
    idx = 1
    res = []
    for _ in range(t):
        n = int(inp[idx])
        a = inp[idx + 1]
        b = inp[idx + 2]
        idx += 3
 
        p1 = []
        p2 = []
        for i in range(n):
            if a[i] == "1":
                p1.append(i)
            if b[i] == "1":
                p2.append(i)
 
        if len(p1) != len(p2):
            res.append("-1")
            continue
 
        c1 = [0] * len(p1)
        c2 = [0] * len(p2)
        for i in range(len(p1)):
            c1[i] = p1[i] % 2
            c2[i] = p2[i] % 2
 
        if sorted(c1) != sorted(c2):
            res.append("-1")
            continue
 
        e1, o1, e2, o2 = [], [], [], []
        for i in range(len(p1)):
            if p1[i] % 2 == 0:
                e1.append(p1[i])
            else:
                o1.append(p1[i])
            if p2[i] % 2 == 0:
                e2.append(p2[i])
            else:
                o2.append(p2[i])
 
        ans = 0
        for i in range(len(e1)):
            ans += abs(e1[i] - e2[i]) // 2
        for i in range(len(o1)):
            ans += abs(o1[i] - o2[i]) // 2
 
        res.append(str(ans))
 
    print("\n".join(res))
 
 
if __name__ == "__main__":
    sol()