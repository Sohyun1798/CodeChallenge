def QueryMatch(info_table, query_table):

    answer = [0]*len(query_table)

    for i in range(len(query_table)):
        for j in range(len(info_table)):
            if query_table[i][4] == '-' or int(info_table[j][4]) >= int(query_table[i][4]):
                if set(query_table[i][:4]) - set(info_table[j][:4]) == {'-'} or set(query_table[i][:4]) - set(info_table[j][:4]) == set():
                    answer[i] += 1

    return answer

def solution(info, query):
    info_table = []
    query_table = []

    for i in range(len(info)):
        temp = info[i].split(" ")
        info_table.append(temp)

    for i in range(len(query)):
        txt = query[i].replace("and ", "")
        temp = txt.split(" ")
        while "" in temp:
            temp.remove("")
        query_table.append(temp)

    answer = QueryMatch(info_table, query_table)

    return answer

