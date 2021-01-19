import sys
sys.setrecursionlimit(10**9)
 
 
N,R,Q=map(int,sys.stdin.readline().split())
Tree=[[] for _ in range(N+1)]
node_count=[0] * (N+1)
check=[True for _ in range(N+1)]
 
 
for _ in range(N-1):
    U,V=map(int,sys.stdin.readline().split())
    Tree[U].append(V)
    Tree[V].append(U)
 
 
def count_node(r):
    node_count[r]=1
    for node in Tree[r]:
        if not node_count[node]:
            count_node(node)
            node_count[r]+=node_count[node]
    return
 
count_node(R)
 
 
for _ in range(Q):
    q=int(sys.stdin.readline())
    print(node_count[q])