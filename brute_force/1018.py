# chess board: WB
wb = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

# chess board: BX
bw = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

def get_input():

   N, M = map(int, input().split()) #map(fun, iter)
   input_matrix = [list(input()) for _ in range(N)]
   
   return N, M, input_matrix

def compare(wb, bw, matrix):
    
    wb_cnt = 0
    bw_cnt = 0

    for i in range(8):
        for j in range(8):
            if wb[i][j] != matrix[i][j]:
                wb_cnt = wb_cnt + 1
            if bw[i][j] != matrix[j][i]:
                bw_cnt = bw_cnt + 1

    return min(wb_cnt, bw_cnt)

def main():

    min_answer = 64
    temp_matrices = []

    N, M, input_matrix = get_input()

    for i in range(0, N-7):
        for j in range(0, M-7):
            temp = []
            temp.append(input_matrix[i][j:j+8])
            temp.append(input_matrix[i+1][j:j+8])
            temp.append(input_matrix[i+2][j:j+8])
            temp.append(input_matrix[i+3][j:j+8])
            temp.append(input_matrix[i+4][j:j+8])
            temp.append(input_matrix[i+5][j:j+8])
            temp.append(input_matrix[i+6][j:j+8])
            temp.append(input_matrix[i+7][j:j+8])

            temp_matrices.append(temp)

    for matrix in temp_matrices:

        answer = compare(wb, bw, matrix)

        if min_answer > answer:
            min_answer = answer

        matrix.clear()

    return print(min_answer) 

if __name__ == "__main__":
    main()
