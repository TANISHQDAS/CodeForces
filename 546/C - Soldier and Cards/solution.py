from collections import deque
n=int(input())
k1,*a=map(int,input().split())
k2,*b=map(int,input().split())
q1,q2=deque(a),deque(b)
seen=set()
for step in range(10**6):
    if not q1:
        print(step,2)
        break
    if not q2:
        print(step,1)
        break
    s=(tuple(q1),tuple(q2))
    if s in seen:
        print(-1)
        break
    seen.add(s)
    x,y=q1.popleft(),q2.popleft()
    if x>y:
        q1.append(y)
        q1.append(x)
    else:
        q2.append(x)
        q2.append(y)