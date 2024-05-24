n,m=map(int,input().split())
#n is no of nodes
#m is no of edges
adj=[]
print(adj)
for i in range(n+1):
    eachRow=[0]*(n+1)
    adj.append(eachRow)
print(adj)
for i in range(m):
    u,v=map(int,input().split())
    adj[u][v]=1
    adj[v][u]=1
print(adj)







# output
# 5 5
# []
# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# 1 3
# 1 2
# 3 4
# 5 1
# 2 5
# [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0]]