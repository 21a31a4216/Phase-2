n,m=map(int,input().split())
#n is no of nodes
#m is no of edges
adj=[]
for i in range(n+1):
    adj.append([])
for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
print(adj)






# output
# 5 5
# 1 2
# 1 3
# 3 4
# 2 4 
# 1 5 
# [[], [2, 3, 5], [1, 4], [1, 4], [3, 2], [1]]