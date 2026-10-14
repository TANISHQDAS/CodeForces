import sys
 
def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1]); idx += 2
        a = data[idx:idx+n]; idx += n
        a = list(map(int, a))
        b = data[idx:idx+m]; idx += m
        b = list(map(int, b))
        b.sort()
        
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + a[i-1]
        
        total = 0
        prev = 0
        for val in b:
            seg_sum = prefix[val] - prefix[prev]
            total += abs(seg_sum)
            prev = val
        
        total += prefix[n] - prefix[prev]
        
        out.append(str(total))
    
    print('
'.join(out))
 
solve()