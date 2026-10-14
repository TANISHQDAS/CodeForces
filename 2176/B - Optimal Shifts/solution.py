import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if '0' not in s:
        print(0)
        continue
 
    s2 = s + s
    max_zeros = 0
    cur = 0
 
    for c in s2:
        if c == '0':
            cur += 1
            max_zeros = max(max_zeros, cur)
        else:
            cur = 0
 
    max_zeros = min(max_zeros, n)
    print(max_zeros)