t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()
 
    ones = [i+1 for i in range(n) if s[i] == '1']
    zeros = [i+1 for i in range(n) if s[i] == '0']
 
    
    if len(ones) % 2 == 0:
        print(len(ones))
        print(*ones)
        continue
 
    if len(zeros) % 2 == 1 and len(ones) > 0:
        print(len(zeros))
        print(*zeros)
        continue
 
    print(-1)