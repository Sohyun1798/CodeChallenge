def get_input():

    N, R, Q = map(int, input().split())
    node_graph = {i:[] for i in range(1, N+1)}

    query = [0]*(Q+1)
    line = []

    for _ in range(N-1):
        left, right = map(int, input().split())
        node_graph[left] += [right]
        node_graph[right] += [left]
      
    for j in range(Q):
        query[j+1] = int(input())

    return N, R, Q, line, query

N, R, Q, line, query = get_input()
print(line)

