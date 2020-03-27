def get_input():

    n = int(input())
    a = []

    for i in range(n):
        a.append(int(input()))

    a = list(set(a))

    return a

def swap(a, b):

    if a > b:
        temp = a
        a = b
        b = temp

def bubble_sort(input_list):

    for i in range(0, len(input_list)-1):
        swap(input_list[i],input_list[i+1])

    return input_list

def main():

    input_list = get_input()
    result = bubble_sort(input_list)

    for i in range(len(input_list)):
        print(result[i])

if __name__ == "__main__":
    main()
    






    



