def max_reachable_nodes(n,edges,restricted):
    from collections import defaultdict
    graph=defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].appned(a)


n=int(input())
edges=[map(int,input().split()) for _ in range(n-1)]
restricted=set(input().split())
