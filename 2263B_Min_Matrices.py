import sys
 
def slv():
    inp = sys.stdin.buffer.read().split()
    p = 0
    t = int(inp[p]); p += 1
    res = []
    for _ in range(t):
        n = int(inp[p]); k = int(inp[p+1]); p += 2
        if k < n or k > 2*n - 1:
            res.append("-1")
            continue
        d = 2*n - k
        mat = [[0]*n for _ in range(n)]
        for i in range(1, d+1):
            mat[i-1][i-1] = i
        for i in range(d+1, n+1):
            mat[i-1][0] = i
        for j in range(d+1, n+1):
            mat[0][j-1] = n - d + j
        f = 2*n - d + 1
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                    mat[i][j] = f
                    f += 1
        for row in mat:
            res.append(' '.join(map(str, row)))
    sys.stdout.write('\n'.join(res) + '\n')
 
slv()