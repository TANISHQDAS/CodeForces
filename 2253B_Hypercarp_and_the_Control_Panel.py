import sys
 
input = sys.stdin.read
 
 
def f(a):
  b, m1_v, m1_d, m2_v, m2_d, ans = {}, None, 0, None, 0, 1
  for x in a:
    if x != m1_v:
      m2_v, m2_d = m1_v, m1_d
      m1_v, m1_d = x, m1_d + 1
  ans = m1_d
  return ans
 
 
def g(n, a):
  r = f(a)
  if n < 2:
    return r
 
  def h(s, x):
    v1, d1, v2, d2 = s
    if x != v1:
      return (x, d1 + 1, v1, d1)
    return s
 
  def m(u, v):
    u1, u2, u3, u4 = u
    v1, v2, v3, v4 = v
    if u1 != v1:
      return u2 + v2
    else:
      return max(u2 + v4, u4 + v2)
 
  L = [None] * (n + 1)
  L[0] = (None, 0, None, 0)
  for j in range(n):
    L[j + 1] = h(L[j], a[j])
 
  R = [None] * (n + 1)
  R[n] = (None, 0, None, 0)
  for j in range(n - 1, -1, -1):
    R[j] = h(R[j + 1], a[j])
 
  for i in range(n - 1):
    if a[i] == a[i + 1]:
      continue
    s1 = h(L[i], a[i + 1])
    s2 = h(s1, a[i])
    r = max(r, m(s2, R[i + 2]))
  return r
 
 
data = input().split()
if data:
  t = int(data[0])
  idx = 1
  for _ in range(t):
    n = int(data[idx])
    a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
    idx += 1 + n
    print(g(n, a))