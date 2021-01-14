def get_input():

    N, R, Q = map(int, input().split())
    node_graph = {i:[] for i in range(1, N+1)}

    query = [0]*Q

    for _ in range(N-1):
        left, right = map(int, input().split())
        node_graph[left] += [right]
        node_graph[right] += [left]
      
    for j in range(Q):
        query[j] = int(input())

    return N, R, Q, node_graph, query

N, R, Q, line, query = get_input()
print(line)

answer = []

for ele in query:

    stack = [ele]
    result = []

    while stack:

        node = stack.pop()
        result += [node]

        for child in line[node]:

            if child in result or child in stack:
                continue
            else: stack += [child]

    answer.append(len(result))

print(answer)



