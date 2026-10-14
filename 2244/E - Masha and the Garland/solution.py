import sys
 
def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); q = int(data[idx+1]); idx += 2
        s = data[idx].decode(); idx += 1
        
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] + (1 if s[i-1] == s[i] else 0)
        
        for _ in range(q):
            l = int(data[idx]); r = int(data[idx+1]); k = int(data[idx+2]); idx += 3
            m = prefix[r-1] - prefix[l-1]
            required = (m + 1) // 2
            out.append("YES" if k >= required else "NO")
    
    print('
'.join(out))
 
solve()