def get_input():

    N, R, Q = map(int, input().split())

    node_graph = {i:[] for i in range(1, N+1)}
    query = [0]*(Q+1)

    for _ in range(N-1):
        parent, child = map(int, input().split())
        node_graph[parent] += [child]

    for i in range(Q):
        query[i+1] = int(input())

    return N, R, Q, node_graph, query

N, R, Q, node_graph, query = get_input()
print(node_graph)

