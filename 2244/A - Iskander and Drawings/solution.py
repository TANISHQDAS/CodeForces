import sys
 
def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        s = input_data[idx]; idx += 1
        max_run = 0
        cur = 0
        for ch in s:
            if ch == '#':
                cur += 1
                if cur > max_run:
                    max_run = cur
            else:
                cur = 0
        ans = (max_run + 1) // 2  # ceil(max_run/2)
        results.append(str(ans))
    print('
'.join(results))
 
solve()