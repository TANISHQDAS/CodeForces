import sys
 
 
def s(n, m, a, b):
  sa = set(a)
  sb = set(b)
  A = sorted([x for x in sa if x not in sb], reverse=True)
  B = sorted([x for x in sb if x not in sa], reverse=True)
  C = sorted([x for x in sa if x in sb], reverse=True)
  pA = [0]
  for x in A:
    pA.append(pA[-1] + x)
  pB = [0]
  for x in B:
    pB.append(pB[-1] + x)
  pC = [0]
  for x in C:
    pC.append(pC[-1] + x)
 
  def h(N, M):
    if N < 0 or M < 0:
      return -1
 
    def v(k, j):
      return pA[min(len(A), N - k)] + pB[min(len(B), M - j)] + pC[k + j]
 
    def f(k):
      l = 0
      r = min(M, len(C) - k)
      if l > r:
        return -1
      while r - l > 2:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        v1 = v(k, m1)
        v2 = v(k, m2)
        if v1 < v2:
          l = m1
        else:
          r = m2
      ans = -1
      for j in range(l, r + 1):
        val = v(k, j)
        if val > ans:
          ans = val
      return ans
 
    l = 0
    r = min(N, len(C))
    while r - l > 2:
      m1 = l + (r - l) // 3
      m2 = r - (r - l) // 3
      v1 = f(m1)
      v2 = f(m2)
      if v1 < v2:
        l = m1
      else:
        r = m2
    ans = -1
    for k in range(l, r + 1):
      val = f(k)
      if val > ans:
        ans = val
    return max(0, ans)
 
  r1 = h(n, m - 1)
  r2 = h(n - 1, m)
  return max(r1, r2)
 
 
d = sys.stdin.read().split()
if d:
  TestsNumT = int(d[0])
  idx = 1
  for _ in range(TestsNumT):
    n = int(d[idx])
    m = int(d[idx + 1])
    x = int(d[idx + 2])
    y = int(d[idx + 3])
    idx += 4
    a = [int(v) for v in d[idx : idx + x]]
    idx += x
    b = [int(v) for v in d[idx : idx + y]]
    idx += y
    print(s(n, m, a, b))