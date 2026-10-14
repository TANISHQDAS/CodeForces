t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
 
    # count blocks
    blocks = 1
    has_equal = False
 
    for i in range(1, n):
        if s[i] == s[i-1]:
            has_equal = True
        else:
            blocks += 1
 
    # all same
    if blocks == 1:
        print(1)
    elif s[0] == s[-1]:
        print(blocks)
    elif has_equal:
        print(blocks + 1)
    else:
        print(blocks)