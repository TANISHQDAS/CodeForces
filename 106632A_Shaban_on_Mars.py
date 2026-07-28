import sys
 
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    queries = [int(x) for x in data[1:t+1]]
    
    max_m = 1000000
    ans = [0] * (max_m + 1)
    is_prime = [True] * (max_m + 1)
    
    for p in range(2, 1001):
        if is_prime[p]:
            for i in range(p * p, max_m + 1, p):
                is_prime[i] = False
                
    ans[1] = 1
    for p in range(2, max_m + 1):
        if is_prime[p]:
            val = p
            r = 1
            while val <= max_m:
                if (r & (r - 1)) == 0:
                    ans[val] += 1
                r += 1
                val *= p
 
    for i in range(2, max_m + 1):
        ans[i] += ans[i - 1]
 
    out = [str(ans[m]) for m in queries]
    print('\n'.join(out))
 
if __name__ == '__main__':
    solve()