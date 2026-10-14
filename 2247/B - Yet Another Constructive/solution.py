import sys
 
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx+1]); m = int(data[idx+2])
        idx += 3
        if m < k:
            out.append("NO")
            continue
        out.append("YES")
        big = m - k + 1
        arr = []
        for i in range(1, n + 1):
            if i % k == 0:
                arr.append(str(big))
            else:
                arr.append("1")
        out.append(" ".join(arr))
    sys.stdout.write("
".join(out) + "
")
 
main()