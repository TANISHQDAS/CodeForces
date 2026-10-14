import sys
 
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx+n]; idx += n
        b = data[idx:idx+n]; idx += n
        
        equal = True
        p = 0
        cnt1_a = 0
        cnt0_b = 0
        for i in range(n):
            ai = a[i]
            bi = b[i]
            if ai == b'1':
                cnt1_a += 1
            if bi == b'0':
                cnt0_b += 1
            if ai != bi:
                equal = False
                if ai == b'1' and bi == b'0':
                    p += 1
        
        if equal:
            out.append("0")
        elif p % 2 == 1:
            out.append("1")
        elif p > 0:
            out.append("2")
        else:
            if cnt1_a > 0 and cnt0_b > 0:
                out.append("2")
            else:
                out.append("-1")
    
    sys.stdout.write("
".join(out) + "
")
 
main()