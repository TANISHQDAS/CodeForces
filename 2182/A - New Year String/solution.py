import sys
 
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
 
    ans = 10**9
 
    for i in range(n - 3):
        cost = 0
        if s[i] != '2': cost += 1
        if s[i+1] != '0': cost += 1
        if s[i+2] != '2': cost += 1
        if s[i+3] != '6': cost += 1
        ans = min(ans, cost)
 
    occ = []
    for i in range(n - 3):
        if s[i:i+4] == "2025":
            occ.append(i)
 
    if not occ:
        ans = min(ans, 0)
    else:
        m = len(occ)
        cover = [0] * n
        for idx, i in enumerate(occ):
            for p in range(i, i + 4):
                cover[p] |= 1 << idx
 
        dp = {0: 0}
        for p in range(n):
            if cover[p] == 0:
                continue
            new_dp = dict(dp)
            for mask, val in dp.items():
                nmask = mask | cover[p]
                if nmask not in new_dp or new_dp[nmask] > val + 1:
                    new_dp[nmask] = val + 1
            dp = new_dp
 
        full = (1 << m) - 1
        ans = min(ans, dp.get(full, 10**9))
 
    print(ans)