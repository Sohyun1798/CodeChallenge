def get_input():

    N, M, V = map(int, input().split())
    matrix = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        link = list(map(int, input().split()))
        matrix[link[0]][link[1]] = 1
        matrix[link[1]][link[0]] = 1

    return V, matrix

def dfs_1260(current_node, matrix, foot_print):

    foot_print += [current_node]

    for search_node in range(len(matrix[current_node])):

        if matrix[current_node][search_node] and search_node not in foot_print:
            foot_print = dfs_1260(search_node, matrix, foot_print)
        
    return foot_print

def bfs_1260(start, matrix):

    queue = [start]
    foot_print = [start]

    while queue:
        
        current_node = queue.pop(0)

        for search_node in range(len(matrix[current_node])):

            if matrix[current_node][search_node] and search_node not in foot_print:
                foot_print += [search_node]
                queue += search_node
    
    return foot_print
