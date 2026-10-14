import sys
 
def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    res = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = data[idx:idx+n]
        idx += n
        s = sum(int(x) for x in arr)
        if n % 2 == 0 and s % 4 == 0:
            res.append("YES")
        else:
            res.append("NO")
    print("
".join(res))
 
main()