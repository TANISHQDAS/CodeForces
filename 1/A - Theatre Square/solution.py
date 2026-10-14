import math
 
n, m, a = map(int, input().split())
 
tiles_n = math.ceil(n / a)
tiles_m = math.ceil(m / a)
 
print(tiles_n * tiles_m)