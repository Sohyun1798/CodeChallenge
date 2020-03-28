def get_input():

    n = int(input())
    a = []

    for i in range(n):
        a.append(int(input()))

    return a

def bubble_sort(input_list):

    for i in range(0, len(input_list)):
        for j in range(len(input_list)-1, i, -1):
            if input_list[j-1] > input_list[j]:
                input_list[j-1], input_list[j] = input_list[j], input_list[j-1]

    return input_list

def main():

    input_list = get_input()
    result = bubble_sort(input_list)

    for i in range(len(result)):
        print(result[i])

if __name__ == "__main__":
    main()
    






    



