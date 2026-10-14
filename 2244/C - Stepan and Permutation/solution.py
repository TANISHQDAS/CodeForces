import sys
 
def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); x = int(data[idx+1]); y = int(data[idx+2]); idx += 3
        p = data[idx:idx+n]; idx += n
        p = list(map(int, p))
        
        parent = list(range(n))
        rank = [0]*n
        
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
        
        for i in range(n - x):
            union(i, i + x)
        for i in range(n - y):
            union(i, i + y)
        
        ok = True
        for i in range(n):
            v = p[i] - 1
            if find(i) != find(v):
                ok = False
                break
        
        out.append("YES" if ok else "NO")
    
    print('
'.join(out))
 
solve()