import sys
 
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        
        target = k ^ n
        
        if target == 0:
            out.append("YES")
            if n == 1:
                out.append("0")
            else:
                # Place 0 at the end
                p = list(range(1, n)) + [0]
                out.append(" ".join(map(str, p)))
                
        elif target < n:
            out.append("YES")
            if n == 2:
                out.append("0 1")
            else:
                remaining = [i for i in range(1, n) if i != target]
                p = remaining + [0, target]
                out.append(" ".join(map(str, p)))
                
        else:
            highest_bit = target.bit_length() - 1
            A = 1 << highest_bit
            B = target ^ A
            
            if A >= n or B >= A or B >= n:
                out.append("NO")
            else:
                out.append("YES")
                used = {0, A, B}
                remaining = [i for i in range(1, n) if i not in used]
                p = remaining + [0, B, A]
                out.append(" ".join(map(str, p)))
                
    print("
".join(out))
 
if __name__ == '__main__':
    solve()