import sys
 
sys.setrecursionlimit(2000000)
 
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        adj = [[] for _ in range(2 * n + 1)]
        
        def add_clause(u, v):
            not_u = -u
            not_v = -v
            
            node_not_u = -u if u < 0 else u + n
            node_v = v if v > 0 else -v + n
            adj[node_not_u].append(node_v)
            
            node_not_v = -v if v < 0 else v + n
            node_u = u if u > 0 else -u + n
            adj[node_not_v].append(node_u)
            
        mag_adj = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)
        
        possible = True
        
        for _ in range(m):
            o = int(data[idx])
            u = int(data[idx+1])
            v = int(data[idx+2])
            idx += 3
            
            if not possible:
                continue
                
            if u == v:
                if o == 1:
                    add_clause(u, u)
                else:
                    add_clause(-u, -u)
            else:
                if o == 1:
                    add_clause(u, v)
                else:
                    add_clause(-u, -v)
 
        visited_time = [0] * (2 * n + 1)
        low = [0] * (2 * n + 1)
        in_stack = [False] * (2 * n + 1)
        stack = []
        scc_id = [0] * (2 * n + 1)
        timer = 0
        scc_counter = 0
        
        def dfs(curr):
            nonlocal timer, scc_counter
            timer += 1
            visited_time[curr] = low[curr] = timer
            stack.append(curr)
            in_stack[curr] = True
            
            for neighbor in adj[curr]:
                if not visited_time[neighbor]:
                    dfs(neighbor)
                    low[curr] = min(low[curr], low[neighbor])
                elif in_stack[neighbor]:
                    low[curr] = min(low[curr], visited_time[neighbor])
                    
            if low[curr] == visited_time[curr]:
                scc_counter += 1
                while True:
                    node = stack.pop()
                    in_stack[node] = False
                    scc_id[node] = scc_counter
                    if node == curr:
                        break
 
        for i in range(1, 2 * n + 1):
            if not visited_time[i]:
                dfs(i)
                
        sign = [0] * (n + 1)
        for i in range(1, n + 1):
            if scc_id[i] == scc_id[i + n]:
                possible = False
                break
            if scc_id[i] < scc_id[i + n]:
                sign[i] = 1
            else:
                sign[i] = -1
 
        if not possible:
            out.append("NO")
            continue
 
        idx_rewind = idx - 3 * m
        for _ in range(m):
            o = int(data[idx_rewind])
            u = int(data[idx_rewind+1])
            v = int(data[idx_rewind+2])
            idx_rewind += 3
            
            if u == v:
                continue
                
            if o == 1:
                if sign[u] == -1 and sign[v] == 1:
                    mag_adj[v].append(u)
                    in_degree[u] += 1
                elif sign[v] == -1 and sign[u] == 1:
                    mag_adj[u].append(v)
                    in_degree[v] += 1
            else:
                if sign[u] == 1 and sign[v] == -1:
                    mag_adj[v].append(u)
                    in_degree[u] += 1
                elif sign[v] == 1 and sign[u] == -1:
                    mag_adj[u].append(v)
                    in_degree[v] += 1
 
        queue = [i for i in range(1, n + 1) if in_degree[i] == 0]
        topo_order = []
        
        while queue:
            curr = queue.pop()
            topo_order.append(curr)
            for neighbor in mag_adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) < n:
            out.append("NO")
            continue
            
        ans = [0] * (n + 1)
        magnitude = 1
        for node in reversed(topo_order):
            ans[node] = sign[node] * magnitude
            magnitude += 1
            
        out.append("YES")
        out.append(" ".join(map(str, ans[1:])))
        
    print("
".join(out))
 
if __name__ == '__main__':
    solve()