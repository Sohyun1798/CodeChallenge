from heapq import heappush, heappop #or just use heapify

def get_input():

    n = int(input())
    input_list = []
    
    for i in range(n):
        input_list.append(int(input()))

    re_dup = list(set(input_list)) #keep in mind set and dict

    return re_dup

def heap_sort(input_list):

    heap = []

    for item in input_list:
        heappush(heap, item)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered

def main():

    input_list = get_input()
    result = heap_sort(input_list)
    
    for i in range(len(result)):
        print(result[i])

if __name__ == "__main__":
    main()
    

